#-*- coding: utf-8 -*-
"""
SMS backend that writes messages to console instead of sending them.

This is a total ripoff of django.core.mail.backends.console
"""
import sys
import threading

from smsing.backends.base import BaseBackend

class SmsBackend(BaseBackend):
    def __init__(self, *args, **kwargs):
        self.stream = kwargs.pop('stream', sys.stdout)
        self._lock = threading.RLock()
        super(SmsBackend, self).__init__(*args, **kwargs)

    def send_messages(self, messages):
        """Write all messages to the stream in a thread-safe way."""
        if not messages:
            return
        self._lock.acquire()
        try:
            # The try-except is nested to allow for
            # Python 2.4 support (Refs #12147)
            try:
                stream_created = self.open()
                for message in messages:
                    self.stream.write(render_message(message))
                    self.stream.write('\n')
                    self.stream.write('-'*79)
                    self.stream.write('\n')
                    self.stream.flush()  # flush after each message
                if stream_created:
                    self.close()
            except:
                if not self.fail_silently:
                    raise
        finally:
            self._lock.release()
        return len(messages)

def render_message(message):
    return u"""to: %(to)s\n%(text)s""" % {
        'to': ", ".join(message.to),
        'text': message.text,
    }

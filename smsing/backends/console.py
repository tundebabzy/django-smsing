#-*- coding: utf-8 -*-
"""
This is basically a fake backend that just writes messages to the
console; no SMS Centers or gateways involved.

This is a total ripoff of django.core.mail.backends.console and inspired
by django-sendsms.

"""
import sys
import threading

from smsing.backends.base import BaseBackend
from smsing.messaging import Message 

class SmsBackend(BaseBackend):
    def __init__(self, *args, **kwargs):
        self.stream = kwargs.pop('stream', sys.stdout)
        self._lock = threading.RLock()
        super(SmsBackend, self).__init__(*args, **kwargs)
        
    def send_messages(self, messages):
        """Write all messages to the stream in a thread-safe way."""
        if not messages:
            return 0
        self._lock.acquire()

        # For a single Message object
        if isinstance(messages, Message):
            messages = [messages]

        # At least lets make sure we are being supplied with a list. We
        # can make sure the list contains Message objects later.
        else:
            assert isinstance(messages, list), 'If you are trying to send \
            a single SMS, supply a Message object else supply a list \
            (or tuple) of Message objects'

        sending_errors = 0
            
        try:
            # The try-except is nested to allow for
            # Python 2.4 support (Refs #12147)
            try:
                stream_created = self.open()
                for message in messages:
                    # Check each element in the list to make sure its
                    # a Message object.
                    if isinstance(message, Message) and message.to:
                        self.stream.write(render_message(message))
                        self.stream.write('\n')
                        self.stream.write('-'*79)
                        self.stream.write('\n')
                        self.stream.flush()  # flush after each message
                    else:
                        self.stream.write('Message sending failed. Invalid message detected.')
                        self.stream.write('\n')
                        self.stream.flush()  # flush after each message
                        sending_errors += 1
                if stream_created:
                    self.close()
            except:
                if not self.fail_silently:
                    raise
        finally:
            self._lock.release()
        return len(messages) - sending_errors

def render_message(message):
    return u"""to: %(to)s\n%(text)s""" % {
        'to': ", ".join(message.to),
        'text': message.text,
    }

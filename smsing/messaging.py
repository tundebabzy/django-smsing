from smsing.api import get_connection

class Message(object):
    """ An SMS message """
    def __init__(self, to=None, text='', connection=None, **kwargs):
        """
        `to` argument should always be a list or tuple.
        `text` argument should be a maximum of 160 characters unless
        kannel has been configured for long messages.
        """
        if to:
            assert not isinstance(to, basestring), 'please use a list or \
            tuple for the `to` argument'
            self.to = to

        else:
            self.to = []

        self.text = text
        self.connection = connection

    def send(self, fail_silently=False):
        """
        Sends an SMS
        """
        if not self.to:
            # Nobody to send to so fail
            return 0
        sent = self.connect(fail_silently).send_messages([self])
        return sent

    def connect(self, fail_silently=False):
        """
        Find a backend connection to use
        """
        if not self.connection:
            self.connection = get_connection(fail_silently=fail_silently)
        return self.connection

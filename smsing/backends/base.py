class BaseBackend(object):
    """
    Base class for backend implementations.

    This should be overridden to create backend implementations.
    """
    def __init__(self, fail_silently=False, **kwargs):
        self.fail_silently = fail_silently

    def get_username(self):
        """
        Returns username for backend authentication where applicable
        """
        pass

    def get_password(self)
        """
        Returns username for backend authentication where applicable
        """
        pass
        
    def send_messages(self, messages):
        """
        Sends one or more Message objects and should return the number
        sent.
        """
        raise NotImplementedError

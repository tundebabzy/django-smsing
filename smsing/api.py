from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module


def get_connection(path=None, fail_silently=False, **kwargs):
    """
    Load an sms backend and return an instance of it.
    """

    path = path or getattr(settings, 'SMSING_BACKEND',
                                'smsing.backends.console.SmsBackend')
    try:
        mod_name, klass_name = path.rsplit('.', 1)
        mod = import_module(mod_name)
    except AttributeError as e:
        raise ImproperlyConfigured(u'Error importing sms backend module %s: "%s"' % (mod_name, e))

    try:
        klass = getattr(mod, klass_name)
    except AttributeError:
        raise ImproperlyConfigured('Module "%s" does not define a "%s" class' % (mod_name, klass_name))

    return klass(fail_silently=fail_silently, **kwargs)

def send_sms(text, to, fail_silently=False,
             username=None, password=None, connection=None):
    """
    A wrapper over Message.send to send an SMS.
    """
    from smsing.messaging import Message
    connection = connection or get_connection(
        fail_silently = fail_silently,
        username = username,
        password = password,
    )
    return Message(text=text, to=to, connection=connection).send()

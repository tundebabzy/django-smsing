from django.conf import settings

def get_connection(path=None, fail_silently=False, **kwargs):
    """
    Load an sms backend and return an instance of it.
    """

    path = path or getattr(settings, 'SMSING_BACKEND')
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

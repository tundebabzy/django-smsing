"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_api_get_connection(self):
        """
        Test api.get_connection and check to see that
        """
        from api import get_connection
        from backends import console
        from django.core.exceptions import ImproperlyConfigured
        
        connection = get_connection()
        self.assertIsInstance(connection, console.SmsBackend)
        connection = get_connection('smsing.backends.console.SmsBackend')
        self.assertIsInstance(connection, console.SmsBackend)
        self.assertRaises(ImproperlyConfigured, get_connection,
                            'smsing.backends.base.SmsBackend')
        
    def test_message(self):
        from messaging import Message
        new_msg = Message(to=['0805'], text='Holla if console backend works')
        new_msg.send()

        new_msg = Message(to=['0805'], text='Holla if console backend works \
            but this time a message that is more than one hundred and \
            sixty characters. For a backend like the console backend, \
            this should not be an issue but with real backends, this \
            might break things.')
        new_msg.send()

        new_msg = Message(to=['0805'], text=' ')
        new_msg.send()

        new_msg = Message(text='Empty `to` field')
        new_msg.send()

    def test_api_send_message(self):
        from api import send_sms
        text = 'Backend message'
        to = ['0703']
        send_sms(text=text, to=to)

        text = ''
        send_sms
        text = """Holla if console backend works but this time a message
            that is more than one hundred and sixty characters. For a
            backend like the console backend, this should not be an
            issue but with real backends, this might break things."""
        send_sms(text=text, to=to)

        to = []
        send_sms(text=text, to=to)

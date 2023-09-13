# contact/tests.py
from django.test import TestCase
from django.core import mail

class ContactGetTest(TestCase):
    def test_contact_form_view(self):
        response = self.client.get('/contato/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact_form.html')

class ContactPostValidTest(TestCase):
    def test_valid_contact_form_submission(self):
        form_data = {
            'name': 'teste',
            'phone': '123456789',
            'email': 'teste@exemplo.com',
            'message': 'testezinho'
        }

        response = self.client.post('/contato/', data=form_data)
        self.assertRedirects(response, '/contato/')

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Confirmação de contato')

class ContactPostInvalidTest(TestCase):
    def test_invalid_contact_form_submission(self):
        form_data = {}  

        response = self.client.post('/contato/', data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact_form.html')

class ContactEmailTest(TestCase):
    def test_contact_email_sent(self):
        form_data = {
            'name': 'teste',
            'phone': '123456789',
            'email': 'teste@exemplo.com',
            'message': 'testezinho'
        }

        response = self.client.post('/contato/', data=form_data)
        self.assertRedirects(response, '/contato/')

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Confirmação de contato')

        body = mail.outbox[0].body

        name = 'Nome: teste'
        phone = 'Telefone: 123456789'
        email = 'Email: teste@exemplo.com'
        message = 'Mensagem:\n\ntestezinho'

        self.assertIn(name, body)
        self.assertIn(phone, body)
        self.assertIn(email, body)
        self.assertIn(message, body)




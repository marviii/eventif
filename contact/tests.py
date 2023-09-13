# contact/tests.py
from django.test import TestCase
from django.core import mail
import re

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

        email_body = str(mail.outbox[0].body)

        self.assertTrue(re.search(r'Nome: teste', email_body))
        self.assertTrue(re.search(r'Telefone: 123456789', email_body))
        self.assertTrue(re.search(r'Email: teste@exemplo.com', email_body))
        self.assertTrue(re.search(r'Mensagem:\n\ntestezinho', email_body))





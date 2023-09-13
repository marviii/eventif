# contact/tests.py
from django.test import TestCase
from django.core import mail
import email
from email import policy

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

        # Obtemos o corpo do e-mail como string
        email_body = str(mail.outbox[0].body)

        # Usamos a biblioteca email para analisar o e-mail
        msg = email.message_from_string(email_body, policy=policy.default)

        # Verificamos se as informações estão no corpo do e-mail
        self.assertIn('Nome: teste', msg.get_payload())
        self.assertIn('Telefone: 123456789', msg.get_payload())
        self.assertIn('Email: teste@exemplo.com', msg.get_payload())
        self.assertIn('Mensagem:\n\ntestezinho', msg.get_payload())




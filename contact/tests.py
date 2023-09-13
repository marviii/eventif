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
    def setUp(self):
        form_data = {
            'name': 'teste',
            'email': 'teste@exemplo.com',
            'phone': '123456789',
            'message': 'testezinho'
        }
        self.response = self.client.post('/contato/', data=form_data)
        self.email = mail.outbox[0]

    def test_contact_email_subject(self):
        expect = 'Confirmação de contato'
        self.assertEqual(expect, self.email.subject)

    def test_contact_email_sender(self):
        expect = 'contato@eventif.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_contact_email_to(self):
        expect = ['contato@eventif.com.br', 'teste@exemplo.com']
        self.assertEqual(expect, self.email.to)

    def test_contact_email_body(self):
        expected_contents = [
            'Novo contato recebido de teste.',
            'Email: teste@exemplo.com',
            'Telefone: 123456789',
            'Nome: teste',
            'Mensagem:\n\ntestezinho',
            'Em até 48 horas úteis alguem da nossa equipe responderá o seu contato.',
            'Atenciosamente,',
            '--',
            'Equipe Eventif'
        ]

        for content in expected_contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
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
        data = dict(
            name = 'teste',
            email = 'teste@exemplo.com',
            phone = '123456789',
            message = 'testezinho'
        )
        self.response = self.client.post('/contato/', data)
        self.email = mail.outbox[0]

    def test_mail_subject(self):
        expect = 'Nova mensagem de teste'
        self.assertEqual(self.email.subject, expect)

    def test_mail_sender(self):
        expect = 'teste@exemplo.com'
        self.assertEqual(self.email.from_email, expect)

    def test_mail_recipients(self):
        expect = ['contato@eventif.com.br', 'teste@exemplo.com']
        self.assertEqual(self.email.to, expect)

    def test_mail_message(self):
        contents = ('teste', 'teste@exemplo.com', '123456789', 'testezinho')
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
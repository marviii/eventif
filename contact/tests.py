# contact/tests.py
from django.test import TestCase
from django.urls import reverse
from .forms import ContactForm
from unittest.mock import patch
from .views import send_confirmation_email

class ContactGetTest(TestCase):
    def test_contact_form_view(self):
        response = self.client.get(reverse('contact:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact_form.html')

class ContactPostValidTest(TestCase):
    def test_valid_contact_form_submission(self):
        form_data = {
            'name': 'teste',
            'phone': '53984693054',
            'email': 'marcos.freitas@aluno.riogrande.ifrs.edu.br',
            'message': 'testeteste'
        }
        response = self.client.post(reverse('contact:contact'), data=form_data)
        self.assertRedirects(response, '/contato/')
        # Verificar se o e-mail foi enviado pode ser um pouco mais complexo, dependendo da configuração de envio de e-mails no seu ambiente de teste

class ContactPostInvalidTest(TestCase):
    def test_invalid_contact_form_submission(self):
        form_data = {}  # Formulário vazio, o que deveria ser inválido
        response = self.client.post(reverse('contact:contact'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact_form.html')

class ContactEmailTest(TestCase):
    def test_email_sending(self):
        form_data = {
            'name': 'teste',
            'phone': '53984693054',
            'email': 'marcos.freitas@aluno.riogrande.ifrs.edu.br',
            'message': 'testeteste'
        }
        send_confirmation_email(form_data) 
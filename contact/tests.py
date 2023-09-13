# contact/tests.py
from django.test import TestCase
from django.urls import reverse
from .views import contact

class ContactGetTest(TestCase):
    def test_contact_form_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact_form.html')

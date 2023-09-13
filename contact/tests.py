from django.test import TestCase
from django.urls import reverse
from eventif.urls import urlpatterns  # Importe as urlpatterns do arquivo de URLs principal

class ContactGetTest(TestCase):
    def test_contact_form_view(self):
        response = self.client.get('/contato/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact_form.html')

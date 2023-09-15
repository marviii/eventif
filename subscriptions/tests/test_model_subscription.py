from datetime import datetime
from django.test import TestCase
from subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = 'Marcos Vinicius',
            cpf = '12345678901',
            email = 'marcos.freitas@aluno.riogrande.ifrs.edu.br',
            phone = '53912345678'
        )
        self.obj.save()
    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Marcos Vinicius', str(self.obj))
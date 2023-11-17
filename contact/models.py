from django.db import models

class Contact(models.Model):
    name = models.CharField('nome', max_length=200)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=20, blank=True, default='Não informado')
    message = models.TextField('mensagem')
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    reply = models.TextField('resposta')
    updated_at = models.DateTimeField('atualizado em', auto_now=True)
    replied = models.BooleanField('respondido', default=False)

    class Meta:
        verbose_name_plural = 'contatos'
        verbose_name = 'contato'
        ordering = ['-created_at', 'replied',]

    def __str__(self):
        return self.name

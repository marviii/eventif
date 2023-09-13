from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect #, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        return create_contact(request)
    else:
        return show_contact_form(request)

def create_contact(request):
    form = ContactForm(request.POST)

    if not form.is_valid():
        return render(request, 'contact/contact_form.html', {'form': form})

    send_confirmation_email(form.cleaned_data)
    messages.success(request, 'Contato realizado com sucesso!')
    return HttpResponseRedirect('/contato/')

def show_contact_form(request):
    return render(request, 'contact/contact_form.html', {'form': ContactForm()})

def send_confirmation_email(data):
    subject = 'Confirmação de contato'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = data['email']
    template_name = 'contact/contact_email.txt'
    context = data

    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_email, [from_email, to_email])
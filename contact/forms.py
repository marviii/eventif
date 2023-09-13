from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome')
    phone = forms.CharField(label='Telefone')
    message = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    email = forms.EmailField(label='Email')
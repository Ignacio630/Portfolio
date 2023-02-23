from django import forms
from django.db import models
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(label='Nombre', max_length=50)
    email = forms.EmailField(label='Correo Electronico', )
    content = forms.CharField(label='Contenido', widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = ['name', 'email', 'content']
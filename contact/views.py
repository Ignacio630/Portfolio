from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
# Create your views here.


def UserContact(request):
    if request.method == 'GET':
        form = ContactForm()
        context = {
            'form': form,
        }
        return render(request, 'contact/contact.html', context=context)
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'form': form,
                'message': 'Contacto enviado! :3',
            }
            return render(request, 'contact/contact.html', context=context)
    else:
        form = ContactForm()
        context = {
            'form': form,
            'error': 'Error al enviar el mensaje'
        }
        return render(request, 'contact/contact.html', context=context)
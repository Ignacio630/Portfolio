from django.shortcuts import render



def home(request):
    context = {
        'title': 'HOLA MUNDO',
    }
    return render(request, 'home.html', context=context)
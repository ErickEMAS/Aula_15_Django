from django.shortcuts import render

# Create your views here.

def mostrar_index(request):
    nome = 'Erick'
    idade = 22
    qualquer_coisas = [
        'oculo',
        'pastel',
        'flango',
        'garrafa',
        'caneta',
        'tesoura',
        'mil'
    ]

    args = {
        'nome': nome,
        'idade': idade,
        'coisas': qualquer_coisas
    }

    return render(request, 'index.html', args)

def mostrar_sortear(request):
    return render(request, 'sortear_frase.html')
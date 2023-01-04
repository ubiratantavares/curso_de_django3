from django.shortcuts import render


def index(request):
    mensagem = "Esta frase está sendo exibida na página index.html"
    return render(request, 'index.html', {'frase': mensagem})

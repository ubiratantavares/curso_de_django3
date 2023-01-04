from django.shortcuts import render


def index(request):
    mensagem = "Esta frase está sendo exibida pela página index.html de produto."
    return render(request, 'produto/index.html', {'frase': mensagem})


def pagina1(request):
    mensagem = "Esta frase está sendo exibida pela página pagina1.html de produto."
    return render(request, 'produto/pagina1.html', {'frase': mensagem})


def pagina2(request):
    mensagem = "Esta frase está sendo exibida pela página pagina2.html de produto."
    return render(request, 'produto/pagina2.html', {'frase': mensagem})

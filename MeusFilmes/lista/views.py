from django.shortcuts import render, redirect
from .models import Filme
# Create your views here.

def home(request):
    filmes = Filme.objects.all()
    return render(request, 'lista/home.html', {"filmes":filmes})

def cadastrar(request):
    if request.method == 'POST':
        filme = Filme()
        filme.title = request.POST['title']
        filme.ano = request.POST['ano']
        if request.POST['visto'] == "true":
            filme.visto = True
        filme.save()
        return redirect('home')

    else:
        return render(request, 'lista/cadastrar.html')

def deletar(request):
    if request.method == 'POST':
        filme = Filme.objects.filter(title=request.POST['title'])
        filme.delete()
        return redirect('home')
    else:
        return render(request, 'lista/deletar.html')

def modificar(request):
    if request.method == 'POST':
        filme = Filme.objects.filter(title=request.POST['title'])
        if request.POST['visto'] == "true":
            filme.update(visto=True)
        elif request.POST['visto'] == "false":
            filme.update(visto=False)            
        return redirect('home')
    else:
        return render(request, 'lista/modificar.html')

def visto(request):
    filmes = Filme.objects.all()
    return render(request, 'lista/vistos.html', {"filmes":filmes})


from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Contacto
from .forms import ContactoForm, ComentarioForm

def index(request):
    return render(request,"website/singlepage.html")

text = ["Page 1 text","Page 2 text","Page 3 text"]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(text[num-1])
    else:
        raise Http404("No such section")
# Create your views here.


def home_page_view(request):
    context = {'website': Contacto.objects.all()}
    return render(request, 'website/home.html', context)


def nova_tarefa_view(request):
    form = ContactoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:home'))

    context = {'form': form}

    return render(request, 'website/nova.html', context)

def novo_comentario_view(request):
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:home'))

    context = {'form': form}

    return render(request, 'website/comentarios.html', context)

def edita_tarefa_view(request, contacto_id):
    contacto = Contacto.objects.get(id=contacto_id)
    form = ContactoForm(request.POST or None, instance=contacto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:home'))

    context = {'form': form, 'contacto_id': contacto_id}
    return render(request, 'website/edita.html', context)


def apaga_tarefa_view(request, contacto_id):
    Contacto.objects.get(id=contacto_id).delete()
    return HttpResponseRedirect(reverse('website:home'))

def contactos_page_view(request):
	return render(request, 'website/contactos.html')
def musica_page_view(request):
	return render(request, 'website/Musica.html')

def Toys_page_view(request):
	return render(request, 'website/Toys.html')

def sobre_page_view(request):
	return render(request, 'website/sobre.html')

def quizz_page_view(request):
	return render(request, 'website/quizz.html')

def quinta_page_view(request):
	return render(request, 'website/quinta.html')

def jogos_page_view(request):
	return render(request, 'website/jogos.html')


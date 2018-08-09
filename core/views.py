from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Ativo
from .form import FormAtivo

# Create your views here.


def inicial(request):
    pass


def sair(request):
    logout(request)
    return render(request, 'login.html')


@login_required
def AtivoConsulta(request):
    consulta = Ativo.objects.all()
    return render(request, 'consulta/consultar_ativo.html', {'form': consulta})


@login_required
def AtivoCreate(request):
    cadastro = FormAtivo(request.POST or None)

    if cadastro.is_valid():
        cadastro.save()
        return redirect('lista_ativos')
    return render(request, 'cadastro/cadastrar_ativo.html', {'form': cadastro})


@login_required
def AtivoAtualiza(request, id):
    at = get_object_or_404(Ativo, pk=id)
    form = FormAtivo(request.POST or None, instance=at)

    if form.is_valid():
        form.save()
        return redirect('lista_ativos')
    return render(request, 'cadastro/cadastrar_ativo.html', {'form': form})

@login_required
def AtivoDeleta(request, id):
    ativo = get_object_or_404(Ativo, pk=id)
    #form = FormAtivo(request.POST or None, instance=at)

    if request.method == 'POST':
        form.delete()
        return redirect('lista_ativos')

    return render(request, 'delete/deletar_ativo.html', {'del': ativo})

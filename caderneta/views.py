from django.utils import timezone
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

from caderneta.forms import ProfessoresForm, AlunosForm, NotasForm, TurmasForm, DisciplinasForm
from caderneta.models import Professores, Alunos, Notas, Turmas, Disciplinas


class HomeView(TemplateView):
    template_name = 'caderneta/index.html'


def cadastra_professor(requisicao: HttpRequest):
    if requisicao.method == 'GET':
        form = ProfessoresForm()
        return render(
            requisicao,
            template_name='caderneta/professores/cadastra.html',
            context={'form': form}
        )

    elif requisicao.method == 'POST':
        form = ProfessoresForm(requisicao.POST)
        if form.is_valid():
            professor = Professores(**form.cleaned_data)
            professor.save()
            return HttpResponseRedirect(redirect_to='/')


def atualiza_professor(requisicao: HttpRequest, pk: int):
    if requisicao.method == 'GET':
        professor = Professores.objects.get(pk=pk)  # Pega os dados contidos na pk e passa para variavel professor
        form = ProfessoresForm(instance=professor)  # Pega os dados de professor e atualiza dentro do formulario
        return render(
            requisicao,
            template_name='caderneta/professores/atualiza.html',
            context={'form': form}
        )

    elif requisicao.method == 'POST':
        professor = Professores.objects.get(pk=pk)
        form = ProfessoresForm(requisicao.POST, instance=professor)  # Vai pegar os dados da get e atualizar
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(redirect_to=f'/')


def detalhe_professor(requisicao: HttpRequest, pk: int):
    if requisicao.method == 'GET':
        try:
            professor = Professores.objects.get(pk=pk)
        except Professores.DoesNotExist:
            professor = None
        return render(
            requisicao,
            template_name='caderneta/professores/detalhe.html',
            context={'professor': professor}
        )


def lista_professor(requisicao: HttpRequest):
    if requisicao.method == 'GET':
        professores = Professores.objects.all()
        paginator = Paginator(professores, 5)
        page_number = requisicao.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(
            requisicao,
            template_name='caderneta/professores/lista.html',
            context={'professores': professores,
                     'page_obj': page_obj,
                    }
            
        )
    


def exclui_professor(requisicao: HttpRequest, pk: int):
    if requisicao.method == 'GET':
        professor = Professores.objects.get(pk=pk)
        form = ProfessoresForm(instance=professor)
        return render(
            requisicao,
            template_name='caderneta/professores/deleta.html',
            context={'form': form}
        )

    elif requisicao.method == 'POST':
        professor = Professores.objects.get(pk=pk)
        form = ProfessoresForm(requisicao.POST, instance=professor)
        if form.is_valid():
            professor.delete()

            return HttpResponseRedirect(redirect_to='/')


class AlunosCreateView(CreateView):
    template_name = 'caderneta/alunos/novo.html'
    model = Alunos
    form_class = AlunosForm
    success_url = reverse_lazy('caderneta:cadastra_aluno')
    success_msg = 'Aluno Criado com sucesso...'


class AlunosListView(ListView):
    model = Alunos
    template_name = 'caderneta/alunos/lista.html'
    context_object_name = 'alunos'
    paginate_by = 15
    


class AlunosUpdateView(UpdateView):
    model = Alunos
    template_name = 'caderneta/alunos/atualiza.html'
    form_class = AlunosForm
    success_url = reverse_lazy('caderneta:lista_aluno')


class AlunosDeleteView(DeleteView):
    model = Alunos
    template_name = 'caderneta/alunos/deleta.html'
    context_object_name = 'aluno'
    success_url = reverse_lazy('caderneta:lista_aluno')

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None


class NotasCreateview(CreateView):
    model = Notas
    template_name = 'caderneta/notas/novo.html'
    form_class = NotasForm
    success_url = reverse_lazy('caderneta:cadastra_nota')


class NotasDeleteview(DeleteView):
    model = Notas
    template_name = 'caderneta/notas/deleta.html'
    context_object_name = 'nota'
    success_url = reverse_lazy('caderneta:home')


class NotasUpdateView(UpdateView):
    model = Notas
    template_name = 'caderneta/notas/atualiza.html'
    form_class = NotasForm
    success_url = reverse_lazy('caderneta:home')


class NotasListView(ListView):
    model = Notas
    template_name = 'caderneta/notas/lista.html'
    context_object_name = 'notas'
    success_url = reverse_lazy('caderneta:lista_notas')


class TurmaCreateview(CreateView):
    model = Turmas
    template_name = 'caderneta/turmas/novo.html'
    form_class = TurmasForm
    success_url = reverse_lazy('caderneta:cria_turma')


class TurmaListView(ListView):
    model = Turmas
    template_name = 'caderneta/turmas/lista.html'
    context_object_name = 'turmas'


class TurmaDeleteView(DeleteView):
    model = Turmas
    template_name = 'caderneta/turmas/deleta.html'
    context_object_name = 'turma'
    success_url = reverse_lazy('caderneta:lista_turma')


class DisciplinasCreateView(CreateView):
    model = Disciplinas
    template_name = 'caderneta/turmas/nova_disciplina.html'
    form_class = DisciplinasForm
    success_url = reverse_lazy('caderneta:lista_professor')

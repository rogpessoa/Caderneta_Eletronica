from django.urls import path

from caderneta.views import cadastra_professor, atualiza_professor, detalhe_professor, lista_professor, \
    exclui_professor, HomeView, AlunosCreateView, AlunosListView, AlunosUpdateView, AlunosDeleteView, NotasCreateview, \
    NotasUpdateView, TurmaCreateview, NotasListView, NotasDeleteview, TurmaListView, TurmaDeleteView, \
    DisciplinasCreateView

app_name = 'caderneta'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # Professores
    path('professores/novo', cadastra_professor, name='cadastra_professor'),
    path('professores/atualiza/<pk>', atualiza_professor, name='atualiza_professor'),
    path('professores/detalhe/<pk>', detalhe_professor, name='detalhe_professor'),
    path('professores/lista', lista_professor, name='lista_professor'),
    path('professores/deleta/<pk>', exclui_professor, name='deleta_professor'),

    # Alunos
    path('alunos/novo', AlunosCreateView.as_view(), name='cadastra_aluno'),
    path('alunos/lista', AlunosListView.as_view(), name='lista_aluno'),
    path('alunos/atualiza/<pk>', AlunosUpdateView.as_view(), name='atualiza_aluno'),
    path('alunos/deleta/<pk>', AlunosDeleteView.as_view(), name='deleta_aluno'),

    # Notas
    path('notas/novo', NotasCreateview.as_view(), name='cadastra_nota'),
    path('notas/atualiza/<pk>', NotasUpdateView.as_view(), name='atualiza_nota'),
    path('notas/lista', NotasListView.as_view(), name='lista_notas'),
    path('notas/deleta/<pk>', NotasDeleteview.as_view(), name='deleta_nota'),

    # Turmas
    path('turmas/novo', TurmaCreateview.as_view(), name='cria_turma'),
    path('turmas/lista', TurmaListView.as_view(), name='lista_turma'),
    path('turmas/deleta/<pk>', TurmaDeleteView.as_view(), name='deleta_turma'),
    path('turmas/disciplina', DisciplinasCreateView.as_view(), name='cria_disciplina'),



]

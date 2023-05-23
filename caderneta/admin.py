from django.contrib import admin
from caderneta import models

@admin.register(models.Professores)
class ProfessoresAdmin(admin.ModelAdmin):
    list_display ='nome', 'sobrenome', 'matricula_professor', 'disciplinas',
        

@admin.register(models.Alunos)
class AlunosAdmin(admin.ModelAdmin):
    list_display = 'nome', 'sobrenome', 'matricula_aluno', 'turmas'
    list_per_page = 20
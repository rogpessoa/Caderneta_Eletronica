from django import forms

from caderneta.models import Professores, Alunos, Notas, Turmas, Disciplinas


class ProfessoresForm(forms.ModelForm):
    class Meta:
        model = Professores
        fields = '__all__'


class AlunosForm(forms.ModelForm):
    class Meta:
        model = Alunos
        fields = '__all__'
        labels = {
            'matricula_aluno': 'Matricula Aluno'

        }

class NotasForm(forms.ModelForm):
    class Meta:
        model = Notas
        fields = '__all__'



class TurmasForm(forms.ModelForm):
    class Meta:
        model = Turmas
        fields = '__all__'


class DisciplinasForm(forms.ModelForm):
    class Meta:
        model = Disciplinas
        fields = '__all__'

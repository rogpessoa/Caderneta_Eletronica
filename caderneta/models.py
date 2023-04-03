from django.db import models


# professores


class Professores(models.Model):
    nome = models.CharField(max_length=40, null=False, blank=False)
    sobrenome = models.CharField(max_length=60, null=False, blank=False)
    matricula_professor = models.IntegerField(primary_key=True, null=False, blank=False)
    email_professor = models.EmailField(null=False, blank=False, max_length=50)
    turmas = models.ForeignKey('turmas', on_delete=models.CASCADE)
    disciplinas = models.ForeignKey('disciplinas', on_delete=models.CASCADE)

    def __str__(self):
        return f'Professor: {self.nome} {self.sobrenome} - {self.disciplinas}'

    class Meta:
        db_table = 'db_professores'


class Alunos(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)
    sobrenome = models.CharField(max_length=50, null=False, blank=False)
    matricula_aluno = models.IntegerField(primary_key=True, null=False, blank=False)
    turmas = models.ForeignKey('turmas', on_delete=models.CASCADE)

    class Meta:
        db_table = 'db_alunos'

    def __str__(self):
        return f'Aluno: {self.nome} {self.sobrenome} -Matricula: {self.matricula_aluno} - {self.turmas}'


class Notas(models.Model):
    nota = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        null=False,
        blank=False
    )

    unidade = models.CharField(
        max_length=15,
        null=False,
        blank=False
    )

    professores = models.ForeignKey('professores', on_delete=models.CASCADE)
    alunos = models.ForeignKey('alunos', on_delete=models.CASCADE)


class Turmas(models.Model):
    turma = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return f'Turma: {self.turma}'


class Disciplinas(models.Model):
    disciplina = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self):
        return f'Disciplina: {self.disciplina}'

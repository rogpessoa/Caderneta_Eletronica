# Generated by Django 4.1.7 on 2023-04-03 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caderneta', '0007_notas_unidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professores',
            name='disciplina',
        ),
        migrations.AddField(
            model_name='turmas',
            name='disciplina',
            field=models.CharField(default=100, max_length=25),
            preserve_default=False,
        ),
    ]

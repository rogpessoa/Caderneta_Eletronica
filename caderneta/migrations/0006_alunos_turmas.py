# Generated by Django 4.1.7 on 2023-03-30 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caderneta', '0005_turmas'),
    ]

    operations = [
        migrations.AddField(
            model_name='alunos',
            name='turmas',
            field=models.ForeignKey(default=100, on_delete=django.db.models.deletion.CASCADE, to='caderneta.turmas'),
            preserve_default=False,
        ),
    ]

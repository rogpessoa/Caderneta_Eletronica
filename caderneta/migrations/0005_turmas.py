# Generated by Django 4.1.7 on 2023-03-30 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caderneta', '0004_alter_notas_nota'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turmas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turma', models.CharField(max_length=10)),
            ],
        ),
    ]

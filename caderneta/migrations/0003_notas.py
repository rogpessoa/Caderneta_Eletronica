# Generated by Django 4.1.7 on 2023-03-22 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caderneta', '0002_professores_email_professor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField(max_length=3)),
                ('alunos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caderneta.alunos')),
                ('professores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caderneta.professores')),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-04 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caderneta', '0011_professores_disciplinas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notas',
            name='nota',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
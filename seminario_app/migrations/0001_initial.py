# Generated by Django 5.0 on 2023-12-21 02:53

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Inscrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('fecha_inscripcion', models.DateTimeField(default=django.utils.timezone.now)),
                ('estado', models.CharField(choices=[('RESERVADO', 'Reservado'), ('COMPLETADA', 'Completada'), ('ANULADA', 'Anulada'), ('NO ASISTEN', 'No Asisten')], default='RESERVADO', max_length=10)),
                ('observacion', models.TextField(blank=True)),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seminario_app.institucion')),
            ],
        ),
    ]

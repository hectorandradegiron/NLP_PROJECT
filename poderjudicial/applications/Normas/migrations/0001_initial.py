# Generated by Django 3.2.8 on 2021-10-24 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entidad', models.CharField(blank=True, max_length=200, null=True, verbose_name='Entidad:')),
                ('titulo', models.CharField(blank=True, max_length=300, null=True, verbose_name='Titulo:')),
                ('tipo_documento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo Documento:')),
                ('numero_documento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Número:')),
                ('considerando', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Considerandos:')),
                ('resuelve', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Se Resuelve:')),
                ('fecha_documento', models.DateField(blank=True, null=True, verbose_name='Fecha:')),
                ('texto_completo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Texto Completo:')),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Expediente',
                'ordering': ['-id'],
            },
        ),
    ]

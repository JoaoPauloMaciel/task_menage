# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-03 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='nome')),
            ],
        ),
        migrations.CreateModel(
            name='Tarefas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='nome')),
                ('dataEHoraDaInscricao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='dataEHoraDaInscricao')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Projeto')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='nome')),
                ('email', models.EmailField(max_length=200, verbose_name='email')),
                ('senha', models.CharField(max_length=20, verbose_name='senha')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioProjeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Projeto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='tarefas',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Usuario'),
        ),
    ]

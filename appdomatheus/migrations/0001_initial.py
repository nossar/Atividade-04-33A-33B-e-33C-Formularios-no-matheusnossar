# Generated by Django 3.2.13 on 2023-09-25 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BandasFavoritas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('ano_de_inicio', models.IntegerField()),
                ('popularidade', models.IntegerField()),
                ('estilo', models.CharField(choices=[('A', 'Alegre'), ('P', 'Pesado'), ('T', 'Triste')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='MusicosFavoritos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('data_de_nascimento', models.DateField()),
                ('banda', models.CharField(max_length=20)),
                ('instrumento', models.CharField(max_length=20)),
            ],
        ),
    ]
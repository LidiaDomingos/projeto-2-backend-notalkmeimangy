# Generated by Django 4.0.4 on 2022-05-10 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicas', '0003_playlist_musica_playlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='id_pesquisa',
            field=models.IntegerField(null=True),
        ),
    ]

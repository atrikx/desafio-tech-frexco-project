# Generated by Django 3.2.11 on 2022-01-24 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frexco', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fruit',
            old_name='chave_e',
            new_name='regiao',
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
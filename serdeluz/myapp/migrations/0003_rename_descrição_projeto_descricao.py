# Generated by Django 5.1.2 on 2025-01-30 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_projeto_alter_conselho_options_alter_conselho_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projeto',
            old_name='descrição',
            new_name='descricao',
        ),
    ]

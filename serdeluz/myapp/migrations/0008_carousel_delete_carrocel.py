# Generated by Django 4.2.16 on 2025-03-11 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_carrocel_remove_projeto_is_principal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics/%y/%m/%d/')),
                ('title', models.CharField(max_length=150)),
                ('action_name', models.CharField(max_length=50)),
                ('link', models.TextField(blank=True, null=True)),
                ('sub_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Carrocel',
        ),
    ]

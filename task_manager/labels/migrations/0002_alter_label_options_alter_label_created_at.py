# Generated by Django 4.0.6 on 2022-07-31 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='label',
            options={'ordering': ['id'], 'verbose_name': 'Метка', 'verbose_name_plural': 'Метки'},
        ),
        migrations.AlterField(
            model_name='label',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата создания'),
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-26 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mymodel',
            options={'verbose_name': 'MyModel', 'verbose_name_plural': 'MyModels'},
        ),
    ]

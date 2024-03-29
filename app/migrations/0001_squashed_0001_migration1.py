# Generated by Django 5.0.2 on 2024-02-26 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('app', '0001_migration1')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='cars')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

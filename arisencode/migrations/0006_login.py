# Generated by Django 3.2.7 on 2023-11-04 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arisencode', '0005_auto_20231104_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='email@email.com', max_length=254, unique=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
    ]
# Generated by Django 3.2.7 on 2023-11-04 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arisencode', '0003_auto_20231104_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='status',
            field=models.CharField(default='Active', max_length=50),
        ),
    ]

# Generated by Django 3.1.1 on 2020-11-20 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
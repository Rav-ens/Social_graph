# Generated by Django 4.1.5 on 2023-01-08 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputData', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputdata',
            name='age_from',
            field=models.IntegerField(max_length=100, verbose_name='Возрас от'),
        ),
        migrations.AlterField(
            model_name='inputdata',
            name='age_to',
            field=models.IntegerField(max_length=100, verbose_name='возраст до'),
        ),
    ]
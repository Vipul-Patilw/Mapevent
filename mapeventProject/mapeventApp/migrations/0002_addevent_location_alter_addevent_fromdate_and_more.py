# Generated by Django 4.0.3 on 2022-08-17 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapeventApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addevent',
            name='location',
            field=models.CharField(default='', max_length=122),
        ),
        migrations.AlterField(
            model_name='addevent',
            name='fromdate',
            field=models.DateField(max_length=122),
        ),
        migrations.AlterField(
            model_name='addevent',
            name='todate',
            field=models.DateField(max_length=122),
        ),
    ]

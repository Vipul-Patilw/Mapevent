# Generated by Django 4.0.3 on 2022-05-28 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChangePassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_password', models.CharField(max_length=122)),
                ('new_password1', models.CharField(max_length=122)),
                ('newpassword2', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=122)),
                ('eventaddress', models.CharField(max_length=122)),
                ('dtime', models.CharField(max_length=122)),
                ('full_name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('emailowner', models.CharField(max_length=122)),
                ('mobile_number', models.CharField(max_length=122)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=122)),
                ('last_name', models.CharField(max_length=122)),
                ('mobile_number', models.CharField(max_length=122)),
                ('username', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=122)),
                ('gender', models.CharField(max_length=122)),
                ('birthdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SendMoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('emailowner', models.CharField(max_length=122)),
                ('mobile_number', models.CharField(max_length=122)),
                ('address', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=122)),
                ('Loginpassword', models.CharField(max_length=122)),
            ],
        ),
    ]

# Generated by Django 5.0 on 2023-12-10 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('GestionServices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=50)),
                ('employee_id', models.CharField(max_length=10, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=191)),
                ('employee_contact', models.CharField(max_length=30)),
                ('adress', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
                ('assigned_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionServices.service')),
            ],
        ),
    ]

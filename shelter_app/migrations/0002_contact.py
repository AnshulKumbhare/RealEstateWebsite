# Generated by Django 5.0.1 on 2024-01-27 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('middlename', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=80)),
                ('mob1', models.BigIntegerField()),
                ('mob2', models.BigIntegerField()),
                ('address', models.CharField(max_length=200)),
                ('msg', models.CharField(max_length=500)),
            ],
        ),
    ]
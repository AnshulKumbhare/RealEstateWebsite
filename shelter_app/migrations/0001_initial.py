# Generated by Django 5.0.1 on 2024-01-27 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimony', models.CharField(max_length=300)),
                ('tpname', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=30)),
                ('companyname', models.CharField(max_length=50)),
            ],
        ),
    ]
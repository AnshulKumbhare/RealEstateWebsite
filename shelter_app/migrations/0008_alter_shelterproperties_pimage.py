# Generated by Django 5.0.1 on 2024-01-29 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter_app', '0007_shelterproperties'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelterproperties',
            name='pimage',
            field=models.ImageField(upload_to='img/%y'),
        ),
    ]

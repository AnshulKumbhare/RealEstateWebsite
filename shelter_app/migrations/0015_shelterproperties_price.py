# Generated by Django 5.0.1 on 2024-01-30 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter_app', '0014_alter_shelterproperties_pimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelterproperties',
            name='price',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
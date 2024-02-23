# Generated by Django 5.0.1 on 2024-01-29 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter_app', '0006_delete_properties'),
    ]

    operations = [
        migrations.CreateModel(
            name='shelterproperties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('middlename', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('mob1', models.BigIntegerField()),
                ('mob2', models.BigIntegerField()),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('propertyname', models.CharField(max_length=100)),
                ('ptype1', models.CharField(max_length=50)),
                ('ptype2', models.CharField(max_length=50)),
                ('beds', models.IntegerField()),
                ('area', models.IntegerField()),
                ('description', models.CharField(max_length=130)),
                ('pimage', models.ImageField(upload_to='image')),
            ],
        ),
    ]

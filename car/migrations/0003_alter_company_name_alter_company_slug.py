# Generated by Django 4.1.7 on 2023-07-28 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_alter_company_name_alter_company_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]

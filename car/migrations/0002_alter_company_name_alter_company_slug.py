# Generated by Django 4.1.7 on 2023-07-28 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='slug',
            field=models.SlugField(),
        ),
    ]

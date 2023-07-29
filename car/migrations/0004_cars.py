# Generated by Django 4.1.7 on 2023-07-28 13:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_alter_company_name_alter_company_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('photo', models.ImageField(blank=True, upload_to='photo/%y/%m/%d')),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
    ]

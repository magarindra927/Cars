# Generated by Django 4.1.7 on 2023-07-28 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_cars'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='car.company'),
            preserve_default=False,
        ),
    ]

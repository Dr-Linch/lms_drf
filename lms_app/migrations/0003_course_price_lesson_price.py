# Generated by Django 5.0 on 2024-02-25 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.PositiveIntegerField(default=1000000, verbose_name=' Стоимость курса'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='price',
            field=models.PositiveIntegerField(default=500000, verbose_name=' Стоимость урока'),
        ),
    ]

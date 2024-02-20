# Generated by Django 5.0 on 2024-02-20 18:06

import django.db.models.deletion
import payments.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lms_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_payment', models.DateField(default=payments.models.get_date_now, verbose_name='Дата оплаты')),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Сумма оплаты')),
                ('pay_type', models.CharField(choices=[('trans', 'Перевод'), ('cash', 'Наличные')], default='trans', max_length=5, verbose_name='способ оплаты')),
                ('paid_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lms_app.course', verbose_name='Оплаченный курс')),
                ('paid_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lms_app.lesson', verbose_name='Оплаченный урок')),
            ],
            options={
                'verbose_name': 'Платёж',
                'verbose_name_plural': 'Платежи',
            },
        ),
    ]

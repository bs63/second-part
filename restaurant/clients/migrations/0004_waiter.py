# Generated by Django 2.0.7 on 2019-05-06 08:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waiterid', models.TextField()),
                ('lastname', models.CharField(max_length=120)),
                ('firstname', models.CharField(max_length=120)),
                ('Username', models.CharField(max_length=120)),
                ('phone_number_wait', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('password', models.CharField(max_length=120)),
                ('order', models.ManyToManyField(to='clients.Order')),
            ],
        ),
    ]

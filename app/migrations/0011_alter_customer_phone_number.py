# Generated by Django 4.2.6 on 2023-11-29 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_transaction_date_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.IntegerField(blank=True, max_length=15, null=True),
        ),
    ]

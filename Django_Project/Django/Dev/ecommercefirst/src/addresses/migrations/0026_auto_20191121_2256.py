# Generated by Django 2.2.6 on 2019-11-21 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0025_auto_20191121_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('shipping', 'Shipping'), ('billing', 'Billing')], max_length=120),
        ),
    ]

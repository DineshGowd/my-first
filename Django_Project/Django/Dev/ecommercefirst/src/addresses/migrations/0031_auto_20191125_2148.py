# Generated by Django 2.2.6 on 2019-11-25 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0030_auto_20191125_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120),
        ),
    ]

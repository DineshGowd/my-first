# Generated by Django 2.2.6 on 2019-10-25 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0005_auto_20191026_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='billing_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billing.BillingProfile'),
        ),
    ]
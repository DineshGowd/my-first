# Generated by Django 2.2.6 on 2019-10-19 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20191019_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]

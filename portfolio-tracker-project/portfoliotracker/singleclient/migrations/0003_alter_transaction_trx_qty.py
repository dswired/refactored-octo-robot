# Generated by Django 3.2.6 on 2022-05-18 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singleclient', '0002_auto_20220514_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='trx_qty',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=15),
        ),
    ]

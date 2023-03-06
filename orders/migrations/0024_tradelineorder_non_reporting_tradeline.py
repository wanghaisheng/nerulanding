# Generated by Django 3.1.4 on 2021-01-22 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0050_nonreportingtradeline'),
        ('orders', '0023_auto_20210103_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradelineorder',
            name='non_reporting_tradeline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.nonreportingtradeline'),
        ),
    ]

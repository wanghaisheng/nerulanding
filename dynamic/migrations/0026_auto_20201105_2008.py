# Generated by Django 3.1.1 on 2020-11-05 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0025_auto_20201101_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdomain',
            name='phno',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

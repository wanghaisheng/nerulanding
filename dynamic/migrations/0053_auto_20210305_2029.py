# Generated by Django 3.1.7 on 2021-03-05 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0052_subdomain_show_life_insurance'),
    ]

    operations = [
        migrations.AddField(
            model_name='subdomain',
            name='services_link',
            field=models.URLField(default='https://www.youtube.com/watch?v=OBCWpTtbm_0', max_length=300),
        ),
        migrations.AlterField(
            model_name='subdomain',
            name='show_why_buy_from_us',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='subdomain',
            name='webinar',
            field=models.URLField(default='https://youtu.be/eL6sb34CGiM', max_length=300),
        ),
    ]
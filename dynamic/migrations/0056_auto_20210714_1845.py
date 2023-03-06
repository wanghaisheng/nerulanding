# Generated by Django 3.2.5 on 2021-07-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0055_alter_subdomain_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subdomain',
            name='display_first_package',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='display_second_package',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='first_package',
            field=models.CharField(blank=True, default='Forever Free Package', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='first_package_1_bullet_point',
            field=models.CharField(blank=True, default='A free credit card for a year.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='first_package_1_button_link',
            field=models.CharField(blank=True, help_text='paste the link where you want your button to get dirrected to ', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='first_package_1_button_text',
            field=models.CharField(blank=True, default='One Time Payment Option', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='first_package_1_show_button',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='first_package_2_bullet_point',
            field=models.CharField(blank=True, default='A free monthly credit card for a year.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='first_package_2_button_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='first_package_2_button_text',
            field=models.CharField(blank=True, default='One Time Payment Option', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='first_package_2_show_button',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='first_package_3_bullet_point',
            field=models.CharField(blank=True, default='A free monthly credit card for a year.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='first_package_4_bullet_point',
            field=models.CharField(blank=True, default='A free monthly credit card for a year.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='first_package_5_bullet_point',
            field=models.CharField(blank=True, default='A free monthly credit card for a year.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='first_package_6_bullet_point',
            field=models.CharField(blank=True, default='A free monthly credit card for a year.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='first_package_7_bullet_point',
            field=models.CharField(blank=True, default='A free monthly credit card for a year.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='first_package_8_bullet_point',
            field=models.CharField(blank=True, default='A free monthly credit card for a year.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='second_package',
            field=models.CharField(blank=True, default='Business Credit Builder Package', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='second_package_1_bullet_point',
            field=models.CharField(blank=True, default='A free credit card for a year.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='second_package_1_button_link',
            field=models.CharField(blank=True, help_text='paste the link where you want your button to get dirrected to ', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='second_package_1_button_text',
            field=models.CharField(blank=True, default='One Time Payment Option', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='second_package_1_show_button',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='second_package_2_bullet_point',
            field=models.CharField(blank=True, default='A free credit card for a year.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='second_package_2_button_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='second_package_2_button_text',
            field=models.CharField(blank=True, default='One Time Payment Option', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='second_package_2_show_button',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='second_package_3_bullet_point',
            field=models.CharField(blank=True, default='A free credit card for a year.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='second_package_4_bullet_point',
            field=models.CharField(blank=True, default='A free credit card for a year.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='second_package_5_bullet_point',
            field=models.CharField(blank=True, default='A free credit card for a year.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='second_package_6_bullet_point',
            field=models.CharField(blank=True, default='A free credit card for a year.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='second_package_7_bullet_point',
            field=models.CharField(blank=True, default='A free credit card for a year.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='second_package_8_bullet_point',
            field=models.CharField(blank=True, default='A free credit card for a year.', max_length=200, null=True),
        ),
    ]

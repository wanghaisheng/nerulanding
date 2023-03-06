# Generated by Django 3.1.1 on 2020-12-09 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0035_auto_20201209_1416'),
        ('products', '0022_tradelines_tradeline_credit_amount'),
        ('orders', '0019_auto_20201209_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradelineorder',
            name='tradeline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.tradelines'),
        ),
        migrations.AlterField(
            model_name='tradelineorder',
            name='tradeline_tier1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.tier1'),
        ),
        migrations.AlterField(
            model_name='tradelineorder',
            name='tradeline_tier2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.tier2'),
        ),
        migrations.AlterField(
            model_name='tradelineorder',
            name='tradeline_tier3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.tier3'),
        ),
        migrations.AlterField(
            model_name='tradelineorder',
            name='tradeline_tier4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.tier4'),
        ),
    ]

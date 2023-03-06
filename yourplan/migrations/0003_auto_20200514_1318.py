# Generated by Django 3.0.5 on 2020-05-14 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yourplan', '0002_auto_20200429_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affirm',
            name='financed_so_far',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='affirm',
            name='how_much_owed',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='affirm',
            name='payment_left',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='affirm',
            name='payment_terms',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='behalf',
            name='financed_so_far',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='behalf',
            name='how_much_owed',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='behalf',
            name='payment_left',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='behalf',
            name='payment_terms',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='fundboxpay',
            name='financed_so_far',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='fundboxpay',
            name='how_much_owed',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='fundboxpay',
            name='payment_left',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='fundboxpay',
            name='payment_terms',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='invoicefactoringpayment',
            name='financed_so_far',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='invoicefactoringpayment',
            name='how_much_owed',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='invoicefactoringpayment',
            name='payment_left',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='invoicefactoringpayment',
            name='payment_terms',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='klarna',
            name='financed_so_far',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='klarna',
            name='how_much_owed',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='klarna',
            name='payment_left',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='klarna',
            name='payment_terms',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='paypal',
            name='financed_so_far',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='paypal',
            name='how_much_owed',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='paypal',
            name='payment_left',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='paypal',
            name='payment_terms',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='quadpay',
            name='financed_so_far',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='quadpay',
            name='how_much_owed',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='quadpay',
            name='payment_left',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='quadpay',
            name='payment_terms',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='regularpayment',
            name='financed_so_far',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='regularpayment',
            name='how_much_owed',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='regularpayment',
            name='payment_left',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='regularpayment',
            name='payment_terms',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='sezzle',
            name='financed_so_far',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='sezzle',
            name='how_much_owed',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='sezzle',
            name='payment_left',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='sezzle',
            name='payment_terms',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='stripe',
            name='financed_so_far',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='stripe',
            name='how_much_owed',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='stripe',
            name='payment_left',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='stripe',
            name='payment_terms',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='viabill',
            name='financed_so_far',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='viabill',
            name='how_much_owed',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='viabill',
            name='payment_left',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='viabill',
            name='payment_terms',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='yourplan',
            name='estimated_term',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='yourplan',
            name='name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='yourplan',
            name='payment_terms',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='yourplan',
            name='report_to',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='yourplan',
            name='terms',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
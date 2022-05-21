# Generated by Django 3.2.6 on 2022-05-14 06:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advisorid', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('advisor', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'unique_together': {('advisorid',)},
            },
        ),
        migrations.CreateModel(
            name='SecurityAssetClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('security_asset_class', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('[A-Za-z]*$', 'Only alphabetic characters are allowed.')])),
            ],
            options={
                'verbose_name': 'Security Asset Class',
                'verbose_name_plural': 'Security Asset Classes',
                'unique_together': {('security_asset_class',)},
            },
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('securityid', models.CharField(max_length=50)),
                ('isin', models.CharField(blank=True, max_length=50)),
                ('ticker', models.CharField(blank=True, max_length=50)),
                ('unit_of_measure', models.DecimalField(decimal_places=5, max_digits=15, null=True)),
                ('name', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('asset_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='singleclient.securityassetclass')),
            ],
            options={
                'verbose_name_plural': 'Securities',
                'unique_together': {('securityid',)},
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('client_type', models.CharField(choices=[('INDIVIDUAL', 'Individual'), ('CORPORATION', 'Corporation'), ('TRUST', 'Trust'), ('FOUNDATION', 'Foundation')], default='Individual', max_length=50)),
                ('date_opened', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('advisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='singleclient.advisor')),
            ],
            options={
                'unique_together': {('clientid',)},
            },
        ),
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('[A-Za-z]*$', 'Only alphabetic characters are allowed.')])),
            ],
            options={
                'unique_together': {('account_type',)},
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountid', models.CharField(max_length=50)),
                ('account_name', models.CharField(max_length=50)),
                ('date_opened', models.DateField()),
                ('inception_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('account_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='singleclient.accounttype')),
                ('clientid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='singleclient.client')),
            ],
            options={
                'unique_together': {('accountid',)},
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_date', models.DateField()),
                ('trx_type', models.CharField(choices=[('BUY', 'Buy'), ('SELL', 'Sell'), ('DIVIDEND', 'Dividend'), ('INTEREST', 'Interest'), ('DEPOSIT', 'Deposit'), ('WITHDRAWAL', 'Withdrawal')], max_length=50)),
                ('trx_qty', models.DecimalField(decimal_places=5, max_digits=15)),
                ('trx_amt', models.DecimalField(decimal_places=5, max_digits=15)),
                ('trxid', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('comment', models.CharField(max_length=50)),
                ('accountid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='singleclient.account')),
                ('security', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='singleclient.security')),
            ],
            options={
                'unique_together': {('trxid',)},
            },
        ),
        migrations.CreateModel(
            name='SecurityPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=5, max_digits=15)),
                ('date', models.DateField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('securityid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='singleclient.security')),
            ],
            options={
                'unique_together': {('securityid', 'date')},
            },
        ),
    ]

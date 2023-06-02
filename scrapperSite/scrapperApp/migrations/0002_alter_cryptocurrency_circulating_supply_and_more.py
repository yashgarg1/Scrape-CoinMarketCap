# Generated by Django 4.2.1 on 2023-06-02 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapperApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency',
            name='circulating_supply',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='market_cap',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='one_h_percent',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='price',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='seven_d_percent',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='twentyFour_h_percent',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='volume_24h',
            field=models.CharField(max_length=255),
        ),
    ]
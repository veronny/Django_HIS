# Generated by Django 3.2.13 on 2024-02-12 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filiacion', '0006_rename_red_rptvisita_red'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rptvisita',
            name='den',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rptvisita',
            name='num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

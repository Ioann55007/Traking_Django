# Generated by Django 4.1.3 on 2022-12-04 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('element_one', '0007_alter_greet_fees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greet',
            name='fees',
            field=models.DateField(null=True),
        ),
    ]

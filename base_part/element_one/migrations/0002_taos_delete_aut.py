# Generated by Django 4.1.3 on 2022-12-10 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('element_one', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('greet', models.CharField(max_length=10)),
                ('agit', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Aut',
        ),
    ]

# Generated by Django 3.2.16 on 2023-01-01 00:55

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('element_one', '0007_auto_20230101_0306'),
    ]

    operations = [
        migrations.AddField(
            model_name='yutug',
            name='updated_by',
            field=django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

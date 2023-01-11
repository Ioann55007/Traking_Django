# Generated by Django 3.2.16 on 2022-12-31 21:45

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('element_one', '0005_alter_author_last_accessed'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogtemplate',
            name='created_by',
            field=django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blogtemplate',
            name='updated_by',
            field=django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='user_current', to=settings.AUTH_USER_MODEL),
        ),
    ]

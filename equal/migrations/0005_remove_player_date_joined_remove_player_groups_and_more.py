# Generated by Django 5.0.7 on 2024-07-12 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equal', '0004_player_date_joined_player_groups_player_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='player',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='player',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='player',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='player',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='player',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='player',
            name='password',
        ),
        migrations.RemoveField(
            model_name='player',
            name='user_permissions',
        ),
    ]

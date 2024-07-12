# Generated by Django 5.0.7 on 2024-07-12 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30)),
                ('nickname', models.CharField(max_length=30)),
                ('highscore', models.IntegerField()),
                ('item', models.JSONField(default=list)),
                ('gold', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=4)),
                ('difficulty', models.IntegerField()),
            ],
        ),
    ]

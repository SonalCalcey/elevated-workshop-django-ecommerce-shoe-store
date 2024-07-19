# Generated by Django 5.0.6 on 2024-07-17 11:53
from django.contrib.auth.models import User
from django.db import migrations


def create_super_user(apps, schema_editor):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@calcey.com',
            password='Test@123'
        )


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_super_user),
    ]

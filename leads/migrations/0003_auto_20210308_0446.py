# Generated by Django 3.1.4 on 2021-03-08 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_user_is_organiser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_organiser',
            new_name='is_agent',
        ),
    ]

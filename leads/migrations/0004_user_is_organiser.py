# Generated by Django 3.1.4 on 2021-03-08 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_auto_20210308_0446'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_organiser',
            field=models.BooleanField(default=True),
        ),
    ]
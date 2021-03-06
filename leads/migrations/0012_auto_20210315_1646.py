# Generated by Django 3.1.4 on 2021-03-15 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0011_auto_20210315_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='lead',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]

# Generated by Django 3.2.4 on 2022-06-29 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_local'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='open',
            field=models.BooleanField(null=True),
        ),
    ]
# Generated by Django 3.2.4 on 2022-06-29 00:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_contactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=64)),
                ('address', models.TextField()),
                ('opening_hours', models.TextField()),
                ('image_url', models.URLField()),
            ],
        ),
    ]

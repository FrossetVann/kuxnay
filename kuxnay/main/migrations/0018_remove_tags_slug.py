# Generated by Django 4.1.7 on 2023-03-16 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_tags_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='slug',
        ),
    ]
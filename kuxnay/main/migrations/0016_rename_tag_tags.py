# Generated by Django 4.1.7 on 2023-03-12 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_remove_recipes_tag_recipes_tag'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tag',
            new_name='Tags',
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-11 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_tagsblock_recipes_tagsid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='TagsId',
        ),
        migrations.DeleteModel(
            name='TagsBlock',
        ),
    ]
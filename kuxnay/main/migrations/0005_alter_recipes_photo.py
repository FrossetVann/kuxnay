# Generated by Django 4.1.7 on 2023-03-09 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_recipes_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='photo',
            field=models.ImageField(null=True, upload_to='main/static/main/img/recipeimage/', verbose_name='Фото'),
        ),
    ]
# Generated by Django 4.1.7 on 2023-03-09 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_recipes_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='recipe',
            field=models.TextField(max_length=5000, verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='tags',
            field=models.CharField(max_length=200, verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='title',
            field=models.CharField(max_length=40, verbose_name='Название'),
        ),
    ]

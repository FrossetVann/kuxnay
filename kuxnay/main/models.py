from django.db import models

class IpModel(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class Recipes(models.Model):
    title = models.CharField('Название', max_length=40)
    photo = models.ImageField(upload_to="main/static/main/img/recipeimage/", verbose_name="Фото", null=True)
    views = models.ManyToManyField(IpModel , related_name="post_views", blank = True)
    structure = models.ManyToManyField('Structure', blank=True)
    recipe = models.TextField('Рецепт', max_length=5000)
    tag = models.ManyToManyField('Tags', blank=True)

    def __str__(self):
        return self.title

    def total_views(self):
        return self.views.count()

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['-id']


class Tags(models.Model):
    name = models.CharField(max_length=40, db_index=True)

    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = 'Тег'
        ordering = ['-id']

    def __str__(self):
        return self.name

class Structure(models.Model):
    name = models.CharField(max_length=40, db_index=True)

    class Meta:
        verbose_name = 'Состав'
        verbose_name_plural = 'Состав'
        ordering = ['-id']

    def __str__(self):
        return self.name

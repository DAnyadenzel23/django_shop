from django.db import models
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=512)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name



class Sections(models.Model):
    section = models.CharField(max_length=15)


    class Meta:
        ordering = ('section',)
        verbose_name = 'Сечение'
        verbose_name_plural = 'Сечения'


    def __str__(self):
        return str(self.section)


class Products(models.Model):
    sections = models.ManyToManyField('Sections')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=100, db_index=True, unique=True, verbose_name='URL')
    description = models.TextField()
    application = models.TextField()
    image = models.ImageField(upload_to='media/products_images')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)


    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})


class Contacts(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    phone = models.TextField()
    adress = models.CharField(max_length=128)
    image = models.ImageField(upload_to='media/contact_images')

    def __str__(self):
        return f'Город: {self.name}'

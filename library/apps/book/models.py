from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=220, blank=False, null=False)
    nationality = models.CharField(max_length=220, blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['name']

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField('Titulo', max_length=225, blank= False, null =False)
    publication_date = models.DateField('Publication date', blank=False, null=False)
    author_id = models.ManyToManyField(Author)
    creation_date = models.DateField('Creation date', auto_now=True, auto_now_add = False)
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['title']

    def __str__(self):
        return self.title

# Generated by Django 3.1.5 on 2021-01-27 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20210127_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='creation_date',
            field=models.DateField(auto_now=True, verbose_name='Creation date'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='author_id',
        ),
        migrations.AddField(
            model_name='book',
            name='author_id',
            field=models.ManyToManyField(to='book.Author'),
        ),
    ]

# Generated by Django 4.0.5 on 2022-10-07 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favoriteBooksApp', '0002_book_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='updated_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]

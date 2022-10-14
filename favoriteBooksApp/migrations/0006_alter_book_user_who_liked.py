# Generated by Django 4.0.5 on 2022-10-07 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0001_initial'),
        ('favoriteBooksApp', '0005_alter_book_user_who_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='user_who_liked',
            field=models.ManyToManyField(related_name='fav_books', to='userApp.user'),
        ),
    ]

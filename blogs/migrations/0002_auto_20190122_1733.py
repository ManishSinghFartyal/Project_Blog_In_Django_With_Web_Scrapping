# Generated by Django 2.1.5 on 2019-01-22 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='author',
            new_name='Author',
        ),
        migrations.RenameField(
            model_name='blogs',
            old_name='blog',
            new_name='Blog',
        ),
        migrations.RenameField(
            model_name='blogs',
            old_name='created_date',
            new_name='Created_date',
        ),
    ]
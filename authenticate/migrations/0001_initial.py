# Generated by Django 2.1.5 on 2019-01-23 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('userId', models.CharField(max_length=40)),
                ('dob', models.DateField()),
                ('password', models.TextField()),
            ],
        ),
    ]
# Generated by Django 3.0.3 on 2020-06-06 14:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder', models.CharField(default='misc', max_length=200)),
                ('num_of_entries', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Folders/Categories',
            },
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=400)),
                ('date_of_creation', models.DateTimeField(default=datetime.datetime(2020, 6, 6, 19, 37, 57, 563795))),
                ('notes', models.TextField()),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.Folder')),
            ],
        ),
    ]

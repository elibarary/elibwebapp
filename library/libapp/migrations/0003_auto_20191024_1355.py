# Generated by Django 2.2.6 on 2019-10-24 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0002_auto_20191020_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booksmodel',
            name='file',
        ),
        migrations.RemoveField(
            model_name='othermodel',
            name='file',
        ),
        migrations.RemoveField(
            model_name='searchmodel',
            name='file',
        ),
        migrations.RemoveField(
            model_name='thesismodel',
            name='file',
        ),
    ]
# Generated by Django 2.2.2 on 2019-06-07 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_remove_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pub_date',
        ),
    ]
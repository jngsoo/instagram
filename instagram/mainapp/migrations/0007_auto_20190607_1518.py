# Generated by Django 2.2.2 on 2019-06-07 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20190607_1510'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RemoveField(
            model_name='post',
            name='pub_date',
        ),
    ]

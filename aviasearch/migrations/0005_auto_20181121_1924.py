# Generated by Django 2.1.3 on 2018-11-21 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviasearch', '0004_auto_20181121_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aviacompany',
            name='date',
            field=models.CharField(max_length=400),
        ),
    ]

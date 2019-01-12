# Generated by Django 2.1.3 on 2018-11-10 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviasearch', '0002_auto_20181107_0109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aviacompany',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='aviacompany',
            name='published_date',
        ),
        migrations.AddField(
            model_name='aviacompany',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='aviacompany',
            name='plains',
            field=models.CharField(max_length=400, null=True),
        ),
    ]

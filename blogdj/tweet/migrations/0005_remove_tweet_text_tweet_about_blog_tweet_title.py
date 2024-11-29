# Generated by Django 5.1.3 on 2024-11-22 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0004_rename_category_tweet_add_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='text',
        ),
        migrations.AddField(
            model_name='tweet',
            name='about_blog',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='tweet',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]

# Generated by Django 5.1.3 on 2024-11-25 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0008_alter_tweet_about_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='about_blog',
            field=models.TextField(default=''),
        ),
    ]

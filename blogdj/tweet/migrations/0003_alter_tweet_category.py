# Generated by Django 5.1.3 on 2024-11-21 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_tweet_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='category',
            field=models.CharField(choices=[('personal', 'Personal'), ('business', 'Business'), ('food', 'Food'), ('product', 'Product'), ('travel', 'Travel'), ('other', 'Other')], default='other', max_length=20),
        ),
    ]

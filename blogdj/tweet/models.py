from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Tweet(models.Model):
    CATEGORY_CHOICES = [
        ('personal', 'Personal'),
        ('business', 'Business'),
        ('food', 'Food'),
        ('product', 'Product'),
        ('travel', 'Travel'),
        ('other', 'Other'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default='')
    photo = models.ImageField(upload_to="photos/", blank=True, null=True)   
    about_blog = models.TextField(null=True, blank=True)  # Use null=True for text fields
    created_at = models.DateTimeField(auto_now_add=True)
    add_tag = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='other', 
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.add_tag} - {self.user.username} - {self.title}'


class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    user_email= models.EmailField()
    text = models.TextField(max_length=150)
    postof = models.ForeignKey(Tweet,on_delete=models.CASCADE , related_name="comments")

    def __str__(self):
        return f'{self.user_name} {self.user_email}'
from django import  forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment

class TweetForm(forms.ModelForm):
    class Meta:
        model =Tweet
        fields = ['title','photo','add_tag','about_blog',]


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["postof"]
        labels = {
            "user_name":"Your name",
            "user_email":"Your email",
            "text":"Your comment",
        }
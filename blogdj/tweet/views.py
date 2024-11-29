from django.shortcuts import render
from django.urls import reverse

from .models import Tweet
from .forms import TweetForm , UserRegistrationForm , CommentForm
from django.shortcuts import get_object_or_404 ,redirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.generic import DetailView



def tweet_list(request):
    tag = request.GET.get('tag', '')  # Get the tag from query parameters
    if tag:
        # Filter tweets based on the 'add_tag' field
        alltweets = Tweet.objects.filter(add_tag__iexact=tag).order_by('-created_at')# Case-insensitive ma
    else:
        alltweets = Tweet.objects.all()  # If no tag is selected, return all tweets
    
    return render(request, 'tweet_list.html', {'alltweets': alltweets, 'selected_tag': tag})


def recent_tweet(request):
    alltweets=Tweet.objects.all().order_by('-created_at')[:6]
    return render(request,'recent_tweet.html',{"alltweets":
                                             alltweets})

@login_required
def tweet_create(request):
    if request.method=='POST':
        form = TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
      form =  TweetForm()
    return render(request,'tweet_form.html',{'form':form
    })

@login_required
def tweet_edit(request , tweet_id):
    tweet=get_object_or_404(Tweet , pk=tweet_id,user = request.user)
    if request.method=='POST':
        form = TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request,'tweet_form.html',
                  {'form':form })



@login_required
def tweet_delete(request,tweet_id):
     tweet = get_object_or_404(Tweet ,pk=tweet_id,user = request.user)
     if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
     return render(request,'tweet_confirm_delete.html',{
         'tweet':tweet
     })


def register(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()

    return render(request,'registration/register.html',{
         'form':form
     })


@login_required
def profile(request):
    user_tweets = Tweet.objects.filter(user=request.user)  # Assuming 'author' is the FK to User
    return render(request, 'profile.html', {'user_tweets': user_tweets})


@login_required
def profiledetail(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    return render(request, 'profiledetail.html',
                   {'tweet': tweet})



class SinglePostView(DetailView):
    model = Tweet  # The model we want to display (Tweet in this case)
    template_name = 'tweet_detail.html'  # The template to use
    context_object_name = 'tweet'

    def get(self, request, pk):
        tweet = get_object_or_404(Tweet, id=pk)

        context = {
            "tweet": tweet,
            "comment_form": CommentForm(),
            "allthecomments": tweet.comments.all().order_by("-id"),
        }
        return render(request, self.template_name, context)  # Return rendered template with context

    def post(self, request, pk):
        tweet = get_object_or_404(Tweet, id=pk)
        comment_form = CommentForm(request.POST)  # Initialize the comment form with the submitted data
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.postof = tweet  # Associate the comment with the tweet
            
            if request.user.is_authenticated:
                comment.user_name = request.user.username  # Set the logged-in user's name
                comment.user_email = request.user.email  # Set the logged-in user's email
            else:
                # Handle non-logged-in users by using the data from the form fields
                comment.user_name = request.POST.get('user_name')
                comment.user_email = request.POST.get('user_email')

            comment.save()  # Save the comment

            # Redirect to the same page after saving the comment
            return redirect(reverse("tweet_detail", args=[pk]))

        # If the form is not valid, return the same page with the form and errors
        context = {
            "tweet": tweet,
            "comment_form": comment_form,
            "allthecomments": tweet.comments.all().order_by("-id"),
        }
        return render(request, self.template_name, context)  # Return rendered template with context

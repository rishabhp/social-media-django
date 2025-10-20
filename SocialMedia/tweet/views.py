from django.shortcuts import render, redirect, get_object_or_404
from .models import Tweet, Comment
from .forms import TweetForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def all_tweet(request):
    tweets = Tweet.objects.select_related('user').all().order_by('datetime_created')
    return render(request, "tweet/all_tweet.html", {'tweets': tweets})

def search_tweet(request):
    if request.method != 'GET':
        return redirect('home')
    keyword = request.GET.get('keyword', '')
    tweets = Tweet.objects.select_related('user').filter(text__icontains=keyword)
    return render(request, "tweet/search.html", {'tweets': tweets, 'keyword': keyword})

@login_required
def add_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('all_tweet')
    else:
        form = TweetForm()
    return render(request, "tweet/tweet_form.html", {'form': form, 'title': "Add Tweet"})

@login_required
def edit_tweet(request, id):
    tweet_instance = get_object_or_404(Tweet, pk=id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet_instance)
        if form.is_valid():
            form.save()
            return redirect('all_tweet')
    else:
        form = TweetForm(instance=tweet_instance)
    return render(request, "tweet/tweet_form.html", {'form': form, 'title': "Edit Tweet"})

@login_required
def delete_tweet(request, id):
    if request.method == 'POST':
        tweet_instance = get_object_or_404(Tweet, pk=id, user=request.user)
        tweet_instance.delete()
    return redirect('all_tweet')


def view_tweet(request, tweet_id):
    tweet_instance = get_object_or_404(Tweet, pk=tweet_id)
    comments = tweet_instance.comments.order_by('datetime_created')
    return render(request, "tweet/tweet_instance.html", {'tweet': tweet_instance, 'comments': comments})


@login_required
def add_comment(request):
    if request.method == 'POST':
        tweet_id = request.POST.get('tweet_id')
        comment = request.POST.get('comment')
        if comment == "" or len(comment) > 100:
            messages.error(request, "Comment length should be between 0 and 100 characters long.")
            return redirect('view_tweet', tweet_id=tweet_id)
        tweet_instance = get_object_or_404(Tweet, pk=tweet_id)
        comment = Comment.objects.create(user=request.user, comment=comment, tweet=tweet_instance)
        comment.save()
        return redirect('view_tweet', tweet_id=tweet_id)
    return redirect('all_tweet')
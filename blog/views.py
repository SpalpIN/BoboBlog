import re

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post
from .forms import NewCommentForm, NewPostForm


def home_view(request):

    all_posts = Post.objects.all()

    return render(request, 'index.html', {'posts': all_posts})


def post_detail_view(request, post):

    post = get_object_or_404(Post, slug=post)

    allcomments = post.comments.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(allcomments, 5)
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return redirect('/' + post.slug)
    else:
        comment_form = NewCommentForm()
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'allcomments': allcomments,
    }
    return render(request, 'post_detail.html', context)


@login_required(login_url='account:login')
def post_add_view(request):
    if request.method == 'POST':
        post_form = NewPostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = request.user
            new_post.slug = re.sub("[^A-Za-z0-9]", "", new_post.title).lower()
            new_post.save()
            return redirect('/' + new_post.slug)
    else:
        post_form = NewPostForm()
    context = {
        'post_form': post_form,
    }
    return render(request, 'post_add.html', context)

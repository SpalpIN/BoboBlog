from celery import shared_task

from blog.models import Post
from blog.forms import NewCommentForm


@shared_task
def save_comment_task(form_data, post_id):
    comment_form = NewCommentForm(form_data)
    post = Post.objects.get(id=post_id)
    user_comment = comment_form.save(commit=False)
    user_comment.post = post
    user_comment.save()

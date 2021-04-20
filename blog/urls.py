from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home_view, name='homepage'),
    path('<slug:post>/', views.post_detail_view, name='post_detail'),
    path('post/add', views.post_add_view, name='post_add'),
]

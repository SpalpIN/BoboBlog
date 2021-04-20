from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('account/login/', views.login_view, name='login'),
    path('account/signup/', views.signup_view, name='signup'),
    path('account/logout/', views.logout_view, name='logout'),
]

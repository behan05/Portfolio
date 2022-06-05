from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('signup/', views.signup, name='Signup'),
    path('signin/', views.signin, name='Signin'),
    path('contact/', views.contact, name='Contact'),
    path('skill/', views.skill, name='Skill'),
    path("blog/", views.blog, name='Blog'),
    path('support-blog1/', views.supportblog1,name='Support-blog1')
]
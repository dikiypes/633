from django.urls import path
from .views import blog_post_list, blog_post_detail, blog_post_create, blog_post_edit, blog_post_delete

app_name = 'blog'

urlpatterns = [
    path('', blog_post_list, name='blog_post_list'),
    path('create/', blog_post_create, name='blog_post_create'),
    path('<slug:slug>/', blog_post_detail, name='blog_post_detail'),
    path('<slug:slug>/edit/', blog_post_edit, name='blog_post_edit'),
    path('<slug:slug>/delete/', blog_post_delete, name='blog_post_delete'),
]

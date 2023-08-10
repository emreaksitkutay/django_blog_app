from django.urls import path
from . import views

urlpatterns = [
  path('', views.base, name='base'),
  path('login/', views.login_view, name='login'),
  path('register/', views.register_view, name='register'),
  path('posts/', views.posts_view, name='posts'),
  path('create_post/', views.create_post_view, name='create_post'),
  path('delete_post/<int:post_id>/', views.delete_post_view, name='delete_post'),
  path('edit_post/<int:post_id>/', views.edit_post_view, name='edit_post'),
  path('accounts/logout/', views.logout_view, name='logout'),
  path('mainpage/', views.mainpage_view, name='mainpage'),
  path('post/<int:pk>/', views.post_detail, name='post_detail'),
  path('<str:username>/', views.profile_view, name='profile'),
  path('republish_post/<int:post_id>/', views.republish_post_view, name='republish_post'),
]
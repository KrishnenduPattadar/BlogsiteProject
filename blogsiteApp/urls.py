
from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_post, name='create'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('comment/<int:post_id>/', views.comment_on_post, name='comment_on_post'),
    path('comment/edit/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),

]

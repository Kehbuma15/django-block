from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('<slug:slug>/delete/', views.post_delete, name='post_delete'),
    path('signup/', views.signup_view, name='signup'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),  # 👈 Put this LAST
]

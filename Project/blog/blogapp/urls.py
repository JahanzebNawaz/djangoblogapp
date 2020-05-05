from django.urls import path, include
from . import views

app_name = 'blogapp'

urlpatterns = [
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('signup/', views.signup, name='signup'),
  path('', views.index, name='home'),
  path('blog/new/', views.blog, name='blog'),
  path('blog/list/', views.blog_list, name='blog_list'),
  path('blog/page/<int:id>', views.blog_page, name='blog_page'),
  path('blog/update/<int:id>', views.blog_update, name='blog_update'),
  path('blog/delete/<int:id>', views.blog_delete, name='blog_delete'),
]
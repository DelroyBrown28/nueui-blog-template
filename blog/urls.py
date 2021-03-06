from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('search/', views.post_search, name='post_search'),
    path('addcomment/', views.addcomment, name='addcomment'),
    path('<slug:post>/', views.post_single, name='post_single'),
    path('category/<category>', views.CategoryListView.as_view(), name='category'),
    
]


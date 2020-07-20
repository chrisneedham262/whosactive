from django.urls import path
from .views import BlogHomeView, ArticleHomeView, AddPostView, UpdateView

urlpatterns = [
    path('', BlogHomeView.as_view(), name='blogHome'),
    path('<int:pk>/', ArticleHomeView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('edit/<int:pk>', UpdateView.as_view(), name='update_post'),
   
]

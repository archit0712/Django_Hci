from django.urls import path
from . import views
# from .views import PostListView,PostDetailView

urlpatterns = [
    path("" , views.blog_index, name='blog-index'),
    path('about/',views.about, name='blog-about'),
    path('tasks/', views.tasks_index, name='tasks-index'),
    path('<str:name>', views.greet, name='greet'),
    # path('post/<int:pk>/', , name='post-detail')
]
from django.urls import path
from .views import AboutView, AuthorView, TagView, CategoryView, CommentView, PostView, HappyClientsView, HomeView, \
    PostDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('category/', CategoryView.as_view(), name='categories'),
    path('tags/', TagView.as_view(), name='tags'),
    path('authors/', AuthorView.as_view(), name='authors'),
    path('blog/', PostView.as_view(), name='blog'),
    path('comments/', CommentView.as_view(), name='comments'),
    path('about/', AboutView.as_view(), name='about'),
    path('happy', HappyClientsView.as_view(), name='happy')
]

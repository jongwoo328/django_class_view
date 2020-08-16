from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.ArticleList.as_view()),
    path('<int:article_id>/', views.ArticleDetail.as_view()),
    path('<int:article_id>/comment/', views.CommentCreate.as_view()),
    path('<int:article_id>/comment/<int:comment_id>/', views.CommentDetail.as_view()),
]
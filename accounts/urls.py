from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.UserList.as_view()),
    path('<int:user_id>/', views.UserDetail.as_view()), 
    path('<int:user_id>/articles', views.UserArticle.as_view()),
]
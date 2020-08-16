from django.urls import path

from . import views


app_name = 'images'

urlpatterns = [
    path('', views.ImageView.as_view()),
    path('<int:image_id>/', views.ImageDetail.as_view()),
]
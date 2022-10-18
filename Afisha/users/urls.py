from django.urls import path
from users import views


urlpatterns = [
    # path('register/', views.register),
    # path('login/', views.login),
    path('register/', views.RegisterAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
]

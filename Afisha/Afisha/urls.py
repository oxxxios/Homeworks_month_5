from django.contrib import admin
from django.urls import path, include
from movie_app import views
from . import swagger
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('api/v1/directors/', views.directors_view),
    # path('api/v1/directors/<int:id>/', views.director_item_view),
    # path('api/v1/movies/', views.movies_view),
    # path('api/v1/movies/<int:id>/', views.movie_item_view),
    # path('api/v1/movies/reviews/', views.movies_reviews_view),
    # path('api/v1/reviews/', views.reviews_view),
    # path('api/v1/reviews/<int:id>/', views.review_item_view),
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/directors/', views.DirectorListAPIView.as_view()),
    path('api/v1/directors/<int:id>/', views.DirectorItemUpdateDeleteAPIView.as_view()),
    path('api/v1/movies/', views.MovieListAPIView.as_view()),
    path('api/v1/movies/<int:id>/', views.MovieItemUpdateDeleteAPIView.as_view()),
    path('api/v1/movies/reviews/', views.MoviesReviewsListAPIView.as_view()),
    path('api/v1/reviews/', views.ReviewListAPIView.as_view()),
    path('api/v1/reviews/<int:id>/', views.ReviewItemUpdateDeleteAPIView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += swagger.urlpatterns

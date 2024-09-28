# books/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet, FavoriteViewSet, RecommendedBooksView, RegisterView, LoginView

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'favorites', FavoriteViewSet, basename='favorite')

urlpatterns = [
    path('register/', RegisterView.as_view({'post': 'create'}), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('recommended/', RecommendedBooksView.as_view({'get': 'list'}), name='recommended'),
    path('', include(router.urls)),
]

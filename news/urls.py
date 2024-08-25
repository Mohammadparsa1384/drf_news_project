from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("news", views.NewsViewSet, basename="news")
router.register("authors", views.AuthorViewSet, basename="author")

urlpatterns = [
    path('', include(router.urls))
]

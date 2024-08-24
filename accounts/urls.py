from . import views
from django.urls import include, path
from rest_framework.routers import SimpleRouter , DefaultRouter

router = DefaultRouter()
router.register("users", views.UserViewSet, basename="user")

urlpatterns = [
    path('', include(router.urls)),
    # path("users-list/",views.UserListView.as_view(), name="login"),
    # path("user-detail/<int:pk>/", views.UserDetailView.as_view(), name="user_detail")
    
]

from django.urls import include, path
from . import views
from django.contrib import admin
from rest_framework_simplejwt.views import TokenRefreshView
from usuario import views
from .views import MyTokenObtainPairView, UserViewSet, RegisterView, PostViewSet
from rest_framework import routers



router = routers.SimpleRouter()
router.register(r"user", UserViewSet, basename="user")
router.register(r"posts", PostViewSet, basename="posts") 

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('register/', views.RegisterView.as_view()),

    path('test/', views.testEndPoint, name='test'),
    path('', views.getRoutes),
    path('', include(router.urls)),
]

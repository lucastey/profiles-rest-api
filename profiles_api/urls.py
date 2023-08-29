from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name="hello-viewset")

#when the path search gets here, it will respond with the hello api view
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view())
]
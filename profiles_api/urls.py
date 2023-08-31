from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views


#urls.py maps URLs to my views, directing the app to the appropriate view for each URL pattern
#I can define the URL patterns using regular expressions or path converters

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name="hello-viewset")
router.register('profile', views.UserProfileViewSet)

#when the path search gets here, it will respond with the hello api view
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
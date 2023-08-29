from django.urls import path

from profiles_api import views

#when the path search gets here, it will respond with the hello api view
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view())
]
# This is for adding view to our Hello API
from django.conf.urls import url
# adding include
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('Login', views.LoginViewSet, base_name='login')
router.register('feed',views.UserProfileFeedViewSet)
urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'',include(router.urls))
]

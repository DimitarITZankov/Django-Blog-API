from django.urls import path,include
from BlogAPI import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('register', views.CreateProfileViewSet)
router.register('posts', views.UserPostViewSet)

urlpatterns = [
	path('',include(router.urls)),
	path('login/', views.UserLoginApiView.as_view()),
]
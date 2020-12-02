from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('teachers', views.TeacherViewSet,basename='teacher')
router.register('students', views.StudentViewSet,basename='student')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.RegisterAPI.as_view(), name='register'),
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from join.views import LoginView, RegisterView, TaskCreateView, TaskDetailView, UserContactsView, UsersView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/login/', LoginView.as_view(), name='login'),
    path('api/v1/register/', RegisterView.as_view(), name='register'),
    path('api/v1/tasks/', TaskCreateView.as_view(),),
    path('api/v1/tasks/<int:id>/', TaskDetailView.as_view(), name='task-detail'),
    path('api/v1/users/', UsersView.as_view(), name='users'),
    path('api/v1/contacts/', UserContactsView.as_view(), name='user-contacts'),]

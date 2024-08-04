from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from join.views import LoginView, RegisterView, TaskCreateView, TaskDetailView, UserContactsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('tasks/', TaskCreateView.as_view(),),
    path('tasks/<int:id>/', TaskDetailView.as_view(), name='task-detail'),
    path('user/contacts/', UserContactsView.as_view(), name='user-contacts'),]

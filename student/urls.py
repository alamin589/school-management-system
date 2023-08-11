
from django.urls import path

from .views import (
    StudentCreateView,
    StudentListView,
    StudentUpdateView,
    StudentDashboard
)

urlpatterns = [
    path("list", StudentListView.as_view(), name="list"),
    path("create/", StudentCreateView.as_view(), name="create"),
    path("<int:pk>/update/", StudentUpdateView.as_view(), name="update"),
    path(
        'dashboard/',
        StudentDashboard.as_view(),
        name='student_dashboard'
    ),

    
]

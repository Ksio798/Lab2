from django.urls import re_path
from .views import ListView


urlpatterns = [
    re_path("Teacher", ListView, kwargs={"api_name": "Teacher"}),
    re_path("Student", ListView, kwargs={"api_name": "Student"}),
    re_path("Class", ListView, kwargs={"api_name": "Class"}),
    re_path("Grade", ListView, kwargs={"api_name": "Grade"}),
    re_path("Hometask", ListView, kwargs={"api_name": "Hometask"}),
    re_path("Schedule", ListView, kwargs={"api_name": "Schedule"}),
]
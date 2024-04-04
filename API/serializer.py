from rest_framework import fields, serializers
from .models import *

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ("FullName", "Subject")

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Classes
        fields = ("ClassName", "TeacherID")

class StuedentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ("FullName", "ClassID")

class GradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grades
        fields = ("Value","Subject", "Date", "StydentID", "TeacherID")

class HometasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hometasks
        fields = ("Subject", "Date", "Description", "TeacherID", "ClassID")

class SchedulesSerializer(serializers.ModelSerializer):
     class Meta:
        model = Schedules
        fields = ("Date", "ClassID", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday")
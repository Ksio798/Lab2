from django.db import models

class Teachers(models.Model):
    FullName = models.TextField()
    Subject = models.TextField()
    def __str__(self) -> str:
        return self.FullName

class Classes(models.Model):
    ClassName = models.TextField()
    TeacherID = models.ForeignKey(Teachers,on_delete = models.DO_NOTHING)
    def __str__(self) -> str:
        return self.ClassName

class Students(models.Model):
    FullName = models.TextField()
    ClassID = models.ForeignKey(Classes,on_delete = models.CASCADE)
    def __str__(self) -> str:
        return self.FullName

class Grades(models.Model):
    Value = models.IntegerField()
    Subject = models.TextField()
    Date = models.DateTimeField()
    StydentID = models.ForeignKey(Students,on_delete = models.CASCADE)
    TeacherID = models.ForeignKey(Teachers,on_delete = models.DO_NOTHING)

class Hometasks(models.Model):
    Subject = models.TextField()
    Description = models.TextField()
    Date = models.DateTimeField()
    ClassID = models.ForeignKey(Classes,on_delete = models.CASCADE)
    TeacherID = models.ForeignKey(Teachers,on_delete = models.DO_NOTHING)

class Schedules(models.Model):
    Date = models.DateTimeField()
    ClassID = models.ForeignKey(Classes,on_delete = models.CASCADE)
    Monday = models.TextField()
    Tuesday = models.TextField()
    Wednesday = models.TextField()
    Thursday = models.TextField()
    Friday = models.TextField()
    Saturday = models.TextField()
from django.db import models

# Create your models here.

class Student(models.Model):

    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    
    # This will return the user name on the admin panel students model section 
    def __str__(self):
        return self.name 


class Task(models.Model):

    student_reference = models.ForeignKey(Student, related_name = 'all_tasks', null = True, on_delete = models.CASCADE)
    task_name = models.CharField(max_length = 100)
    description = models.TextField()

    def __str__(self):
        return self.task_name
    

class RankSheet(models.Model):

    tamil = models.IntegerField()
    english = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    social_science = models.IntegerField()
    total = models.IntegerField()
    average = models.FloatField()
    result = models.CharField(max_length = 10)
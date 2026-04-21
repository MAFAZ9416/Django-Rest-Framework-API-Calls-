from rest_framework.serializers import ModelSerializer
from .models import *

# Serilalizers

class StudentSerializer(ModelSerializer):

    class Meta:

        model = Student
        fields = '__all__'

class TaskSerializer(ModelSerializer):
    
    class Meta:

        model = Task
        fields = '__all__'

class Student_TaskSerializer(ModelSerializer):

    all_tasks = TaskSerializer(many=True)

    class Meta:

        model = Student
        fields = '__all__'

class Task_StudentSerializer(ModelSerializer):

    student_reference = StudentSerializer()

    class Meta:

        model = Task
        fields = '__all__'

class RankSheetSerializer(ModelSerializer):

    class Meta:

        model = RankSheet
        fields = '__all__'

       
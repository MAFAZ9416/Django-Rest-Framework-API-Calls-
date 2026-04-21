from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class StudentAPI(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, student_id = None):

        if student_id is None:
            all_students = Student.objects.all()
            student_list = Student_TaskSerializer(all_students, many = True).data
        else:
            student = Student.objects.get(id = student_id)
            student_list = Student_TaskSerializer(student).data

        return Response(student_list)

    def post(self, request):
        
        new_student = Student(name = request.data['name'], age = request.data['age'])
        new_student.save()

        return Response("New Student Created.")
    
    def put(self, request, student_id):

        student_data = Student.objects.filter(id = student_id)
        student_data.update(name = request.data['name'], age = request.data['age'])

        return Response("Student Data Updated")
    
    def delete(self, request, student_id):

        student_data = Student.objects.get(id = student_id)
        student_data.delete()

        return Response("Student Data Deleted")


class TaskView(APIView):

    def get(self, request, task_id = None):

        if task_id == None :
            task = Task.objects.all()
            task_data = Task_StudentSerializer(task, many = True).data
        else :
            task = Task.objects.get(id = task_id)
            task_data = Task_StudentSerializer(task).data

        return Response(task_data)

    def post(self, request):

        post_data = TaskSerializer(data = request.data)

        if post_data.is_valid():

            post_data.save()
            return Response("New Task Created")
        
        else:
            return Response(post_data.errors)
    
    def put(self, request, task_id):

        task = Task.objects.get(id = task_id)
        update_data = TaskSerializer(task, data = request.data, partial = True)

        if update_data.is_valid():

            update_data.save()
            return Response("Task Updated")
        
        else:
            return Response(update_data.errors)
        
    def patch(self, request, task_id):

        task = Task.objects.get(id = task_id)
        update_data = TaskSerializer(task, data = request.data, partial = True)

        if update_data.is_valid():

            update_data.save()
            return Response("Task Updated")
        
        else:
            return Response(update_data.errors)
        
    def delete(self, request, task_id):

        task = Task.objects.get(id = task_id)
        task.delete()

        return Response("Task Deleted")
    

class RankSheetView(APIView):

    # We have the same codes on the post and put and patch methods so if we worte in a function then we avoid to write multiple time just simple call the common_code function to just that.
    def common_code(self, request):

        # Common codes for those function
        total = request.data['tamil'] + request.data['english'] + request.data['maths'] + request.data['science'] + request.data['social_science']

        average = total/5
        
        if (request.data['tamil'] >= 35) and (request.data['english'] >= 35) and (request.data['maths'] >= 35) and (request.data['science'] >= 35) and (request.data['social_science'] >= 35) :

            result = 'Pass'

        else :
            result = 'Fail'

        return total,average,result

    def get(self, request, rank_id = None):

        if not rank_id:
            rank = RankSheet.objects.all()
            all_rank = RankSheetSerializer(rank, many = True).data

        else:
            rank = RankSheet.objects.get(id = rank_id)
            all_rank = RankSheetSerializer(rank).data

        return Response(all_rank)

    def post(self, request):

        # Function Call
        total, average, result = self.common_code(request)
        
        rank_data = RankSheet(tamil = request.data['tamil'], english = request.data['english'], maths = request.data['maths'], science = request.data['science'],social_science = request.data['social_science'], total = total, average = average, result = result)

        rank_data.save()

        return Response("Student Record Saved Successfully!....")

    def put(self, request, rank_id):

        rank = RankSheet.objects.filter(id = rank_id)

        # Function Call
        total, average, result = self.common_code(request)

        rank.update(tamil = request.data['tamil'], english = request.data['english'], maths = request.data['maths'], science = request.data['science'],social_science = request.data['social_science'], total = total, average = average, result = result)

        return Response("Student Record Updated!...")

    def patch(self, request, rank_id):

        rank = RankSheet.objects.filter(id = rank_id)

        # Function Call
        total, average, result = self.common_code(request)

        rank.update(tamil = request.data['tamil'], english = request.data['english'], maths = request.data['maths'], science = request.data['science'],social_science = request.data['social_science'], total = total, average = average, result = result)

        return Response("Student Record Updated!...")

    def delete(self, request, rank_id):

        rank_data = RankSheet.objects.get(id = rank_id)
        rank_data.delete()
        return Response("Student Record Deleted Successfully!...")


# Using Function to handle the api get,put,post,patch,delete methods

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def API(request, id = None):

    if request.method == 'GET' :
        if not id:
            task = Task.objects.all()
            task_data = TaskSerializer(task, many = True).data
        else:
            task = Task.objects.get(id = id)
            task_data = TaskSerializer(task).data
        return Response(task_data)
    
    elif request.method == 'POST' :
        task = TaskSerializer(data = request.data)

        if task.is_valid():
            task.save()
            return Response("Task Created.")
        

        else :
            return Response(task.errors)

    elif request.method == 'PUT' :
        task = Task.objects.get(id = id)
        task_data = TaskSerializer(task, data = request.data, partial = True)

        if task_data.is_valid():
            task_data.save()
            return Response("Task Updated.")
        
        else :
            return Response(task_data.errors)
        
    elif request.method == 'PATCH' :
        task = Task.objects.get(id = id)
        task_data = TaskSerializer(task, data = request.data, partial = True)

        if task_data.is_valid():
            task_data.save()
            return Response("Task Updated.")
        
        else :
            return Response(task_data.errors)
        
    elif request.method == 'DELETE' :
        task = Task.objects.get(id = id)
        task.delete()
        return Response('Task Deleted.')
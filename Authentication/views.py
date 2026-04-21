from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

# Create your views here.

class UserView(APIView):

    def post(self, request):

        user = User(username = request.data['username'], is_superuser = request.data['is_superuser'])

        user.set_password(request.data['password'])

        user.save()
        return Response("User Registered Successfully.")


class UserLoginView(APIView):

    permisssion_classes = [IsAuthenticated]

    def post(self, request):

        # This is for basic authentication with out using JWT tokens
        # user_verification = authenticate(username = request.data['username'], password = request.data['password'])

        # if user_verification:
        #     return Response("Login Successfully.")

        # else:
        #     return Response("Username or password Invalid please try again.")  

        # This is for JWT token authentication

        user_verification = CustomTokenSerializer(data = request.data)
        
        if user_verification.is_valid() :

            return Response(user_verification.validated_data)
        
        else :
            return Response(user_verification.errors)

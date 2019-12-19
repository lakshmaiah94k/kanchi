from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentAppSerializer, StudentRegSerializer, StaffSerializer, DepartmentSerializer, UserSerializer
from .models import StudentReg, StudentApp, Staff, Department
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated


class StudentAppView(APIView):

    def get(self, request, format=None):
        user = StudentApp.objects.all()
        serializer = StudentAppSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentAppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentRegView(APIView):

    def get(self, request):
        user = StudentReg.objects.all()
        serializer = StudentRegSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentRegSerializer(data=request.data)
        # import pdb;pdb.set_trace()
        if serializer.is_valid():
            user = StudentApp.objects.filter(email=serializer.validated_data['student_email'], is_verified=True)
            if not user.exists():
                return Response(status=status.HTTP_400_BAD_REQUEST)
            serializer.validated_data["student_email"] = user.first()
            serializer.validated_data.pop()
            # serial = UserSerializer(data=request.data)
            # if serial.is_valid():
            #     serial.save()
            #     return Response(serial.data, status=status.HTTP_201_CREATED)
            # users=User.objects.create_user(username=serial.validated_data["student_name"], password=serial.validated_data["password"])
            # serializer.user=serial
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk):
        user = StudentReg.objects.get(id=pk)
        serializer = StudentRegSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentView(APIView):

    def get(self, request):
        user = Department.objects.all()
        serializer = DepartmentSerializer(user, many=True)
        return Response(serializer.data)


class StaffView(APIView):

    def get(self, request):
        user = Staff.objects.all()
        serializer = StaffSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        user = Staff.objects.get(id=pk)
        serializer = StaffSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = Staff.objects.get(id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
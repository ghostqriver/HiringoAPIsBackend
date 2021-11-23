from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response

from .models import StudentBasic, TeacherBasic, UserStudentProfile, UserTeacherProfile,CourseBasic,SubjectBasic
from django.views import View
from .serializers import StudentInfoSerializers, TeacherInfoSerializers, StudentAccountSerializers, \
    TeacherAccountSerializers,CourseInfoSerializers,SubjectInfoSerializers
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from django.utils.timezone import now


# Create your views here.
class APIRootView(APIView):
    def get(self, request):
        year = now().year
        data = {
            'StudentInfo': 'http://127.0.0.1:8000/students/',
            'TeacherInfo': 'http://127.0.0.1:8000/teachers/',
            'StudentAccount': 'http://127.0.0.1:8000/studentsaccount/',
            'TeacherAccount': 'http://127.0.0.1:8000/teachersaccount/',
            'CourseInfo': 'http://127.0.0.1:8000/courses/',
            'SubjectInfo': 'http://127.0.0.1:8000/subjects/'
        }
        return Response(data)


class StudentInfoView(ModelViewSet):
    # 指定查询集
    queryset = UserStudentProfile.objects.all()
    # 指定序列化器
    serializer_class = StudentInfoSerializers


class TeacherInfoView(ModelViewSet):
    queryset = UserTeacherProfile.objects.all()
    serializer_class = TeacherInfoSerializers


class StudentAccountView(ModelViewSet):
    queryset = StudentBasic.objects.all()
    serializer_class = StudentAccountSerializers


class TeacherAccountView(ModelViewSet):
    queryset = TeacherBasic.objects.all()
    serializer_class = TeacherAccountSerializers


class CourseInfoView(ModelViewSet):
    queryset = CourseBasic.objects.all()
    serializer_class = CourseInfoSerializers


class SubjectInfoView(ModelViewSet):
    queryset = SubjectBasic.objects.all()
    serializer_class = SubjectInfoSerializers



import pandas as pd
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required, login_required
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from .permission import HighPermission
from .serializer import *
from .models import *
from rest_framework.viewsets import ModelViewSet

class CourseViewset(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    permission_classes = [IsAdminUser, IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print(f'request.data:{request.data}')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        res = {'code':200, 'msg':'success!'}
        return Response(res)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        res = {'code':204, 'msg':'success!'}
        return Response(res)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        res = {'code':200, 'msg':'success!'}
        return Response(res)



class LecturerViewset(ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    def create(self, request, *args, **kwargs):
        print(f'request.data:{request.data}')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        res = {'code':200, 'msg':'success!'}
        return Response(res)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        res = {'code':204, 'msg':'success!'}
        return Response(res)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        res = {'code':200, 'msg':'success!'}
        return Response(res)


class SemesterViewset(ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print(f'request.data:{request.data}')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        res = {'code':200, 'msg':'success!'}
        return Response(res)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        res = {'code':204, 'msg':'success!'}
        return Response(res)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        res = {'code':200, 'msg':'success!'}
        return Response(res)

class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print(f'request.data:{request.data}')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        res = {'code': 200, 'msg': 'success!'}
        return Response(res)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        res = {'code':204, 'msg':'success!'}
        return Response(res)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        res = {'code':200, 'msg':'success!'}
        return Response(res)


class ClassViewset(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print(f'request.data:{request.data}')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        res = {'code': 200, 'msg': 'success!'}
        return Response(res)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        res = {'code':204, 'msg':'success!'}
        return Response(res)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        res = {'code':200, 'msg':'success!'}
        return Response(res)

class StudentViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    @permission_required('backend.create_student', raise_exception=True)
    def create(self, request, *args, **kwargs):
        print(f'request.data:{request.data}')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        res = {'code': 200, 'msg': 'success!'}
        return Response(res)
    @permission_required('backend.delete_student', raise_exception=True)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        res = {'code':204, 'msg':'success!'}
        return Response(res)
    @permission_required('backend.change_student', raise_exception=True)
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        res = {'code':200, 'msg':'success!'}
        return Response(res)


class LoginViewSet(APIView):
    permission_classes = (AllowAny,)  # AllowAny

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        pwd = request.data.get("password")
        user = authenticate(username=username, password=pwd)
        print(next)
        print(username, pwd)
        if user:
            print(f'user.is_active:{user.is_active}')
            if user.is_active == True:  #
                login(request, user)
                return JsonResponse({"msg":"success!"})
        else:
            return JsonResponse({"msg":"uncorrect!"})


class AssignViewSet(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def put(self, request):
        cid = request.data.get("cid")
        print(f'cid:{cid}')
        lecturer = request.data.get("lecturer")
        l = Lecturer.objects.get(staff_id=lecturer)
        c = Class.objects.get(id=cid)
        c.lecturer = l
        c.save()
        return JsonResponse({"code":200, "msg":"success!"})

class EnrollViewSet(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def put(self, request):
        sid = request.data.get("sid")
        print(f'sid:{sid}')
        myclass = request.data.get("myclass")
        c = Class.objects.filter(number__in=myclass)
        s = Student.objects.get(id=sid)
        s.myclass.set(c)
        s.save()
        return JsonResponse({"code":200, "msg":"success!"})

class AttViewSet(APIView):
    permission_classes = [IsAuthenticated,  HighPermission]
    def put(self, request):
        sid = request.data.get("sid")
        print(f'sid:{sid}')
        attend = request.data.get("attend")
        s = Student.objects.get(id=sid)
        s.attend = attend
        s.save()
        return JsonResponse({"code":200, "msg":"success!"})

class EmailViewSet(APIView):
    permission_classes = [IsAuthenticated, HighPermission]
    def post(self, request):
        print(f're:{request.data}')
        subject = request.data.get("subject")
        content = request.data.get("body")
        to = request.POST.get("to")
        try:
            send_mail(subject=subject, message=content, recipient_list=[to, ], from_email="752785200@qq.com")
            return JsonResponse({"code":200, "msg":"success!"})
        except Exception as e:
            print(e)
            return JsonResponse({"msg":"error"})

class FileViewSet(APIView):
    permission_classes = [IsAuthenticated, HighPermission]
    def post(self, request):
        try:
            stufile = request.data.get("file")
            print(stufile)
            fs = FileSystemStorage()
            file = fs.save(stufile.name, stufile)

            data = pd.read_excel(stufile)
            data = pd.DataFrame(data, columns=[
                "student_id", "attend"
            ])
            stu_id = data["student_id"].tolist()
            attend = data["attend"].tolist()
            for i in range(len(stu_id)):
                student = Student.objects.get(student_id=stu_id[i])
                student.attend = attend[i]
                student.save()
            return JsonResponse({"msg":"success!"})
        except Exception as e:
            print(e)
            return JsonResponse({"msg":"error"})

"""att URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from backend.Viewset import UserViewset, LecturerViewset, SemesterViewset, ClassViewset, \
    StudentViewset, CourseViewset, LoginViewSet, AssignViewSet, EnrollViewSet, AttViewSet, EmailViewSet, FileViewSet

router = SimpleRouter()
router.register("semester", SemesterViewset, "semester")
router.register("course",CourseViewset,"course")
router.register("user",UserViewset,"user"),
router.register("lecturer",LecturerViewset),
router.register("class", ClassViewset),
router.register("student", StudentViewset)

for url in router.urls:
    print(url)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('drf/', include(router.urls)),
    path('login/',LoginViewSet.as_view()),
    path('assign/',AssignViewSet.as_view()),
    path('enroll/', EnrollViewSet.as_view()),
    path('attend/', AttViewSet.as_view()),
    path('email/', EmailViewSet.as_view()),
    path('upload/', FileViewSet.as_view())


]

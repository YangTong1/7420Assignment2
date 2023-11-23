from django.contrib.auth.models import Group, User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import *

class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class UserSerializer(ModelSerializer):
    # groups = GroupSerializer(many=True)
    # grouplist = serializers.ListField(write_only=True)
    groups = serializers.CharField()
    telephone = serializers.CharField(write_only=True,required=False)
    address = serializers.CharField(write_only=True, required=False)
    tel = serializers.SerializerMethodField(required=False)
    addr = serializers.SerializerMethodField(required=False)
    groupname = serializers.SerializerMethodField(required=False)

    def get_tel(self, instance):
        try:
            tel = UserProfile.objects.get(user=instance).telephone
            return tel
        except Exception as e:
            print(e)
            return ""

    def get_addr(self, instance):
        try:
            addr = UserProfile.objects.get(user=instance).address
            return addr
        except Exception as e:
            print(e)
            return ""

    def get_groupname(self, instance):
        gp = list(instance.groups.all())
        print(f'gp:{gp}')
        return gp[0].name

    def create(self, validated_data):
        print("vadata:", validated_data)
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        groups = validated_data.get('groups')
        telephone = validated_data.get('telephone')
        address = validated_data.get('address')
        print(f'Group:{groups}')
        myuser = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                          last_name=last_name)
        mygroup = Group.objects.get(name=groups)
        myuser.groups.add(mygroup)
        UserProfile.objects.create(user=myuser, address=address, telephone=telephone)
        return myuser

    def update(self, instance, validated_data):
        print("vadata:", validated_data)
        username = validated_data.get('username')
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        groups = validated_data.get('groups')
        telephone = validated_data.get('telephone')
        address = validated_data.get('address')
        print(f'Group:{groups}')
        try:
            instance.email = email
            instance.first_name = first_name
            instance.last_name = last_name
            gp = Group.objects.get(name=groups)
            instance.groups.set([gp])  # set方法需要传一个列表
            instance.save()
            up = UserProfile.objects.get(user=instance)
            up.address = address
            up.telephone = telephone
            up.save()
        except Exception as e:
            print(e)
        return instance


    class Meta:
        model = User
        fields = '__all__'


class LecturerSerializer(ModelSerializer):
    user = serializers.CharField()
    firstname = serializers.SerializerMethodField(required=False)

    def get_firstname(self, instance):
        try:
            name = instance.user.first_name
            return name
        except Exception as e:
            print(e)
            return ""

    def create(self, validated_data):
        print("vadata:", validated_data)
        staff_id = validated_data.get('staff_id')
        DOB = validated_data.get('DOB')
        user = validated_data.get('user')
        print(f'Group:{user}')
        myuser = User.objects.get(username=user)
        l = Lecturer.objects.create(staff_id=staff_id, DOB=DOB, user=myuser)
        return l

    def update(self, instance, validated_data):
        print("vadata:", validated_data)
        staff_id = validated_data.get('staff_id')
        DOB = validated_data.get('DOB')
        user = validated_data.get('user')
        myuser = User.objects.get(username=user)
        instance.staff_id = staff_id
        instance.DOB = DOB
        instance.user = myuser
        instance.save()
        return instance

    class Meta:
        model = Lecturer
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    #根据model定义serializer
    class Meta:
        model = Course #指明serializer处理的数据字段是从course这个model里来的
        fields = '__all__' #all表示包含所有的字段

class SemesterSerializer(ModelSerializer):
    course = serializers.CharField()

    mycourse = serializers.SerializerMethodField(required=False)

    def get_mycourse(self, instance):
        cs = instance.course.all()
        cstr = ""
        for c in cs:
            cstr += c.name
            cstr += " "
        return cstr


    def create(self, validated_data):
        print("vadata:", validated_data)
        year = validated_data.get('year')
        semester = validated_data.get('semester')
        course = validated_data.get('course')
        course = course.split(",")
        print(f'Group:{course}')
        courses = Course.objects.filter(name__in=course)
        s = Semester.objects.create(year=year, semester=semester)
        s.course.add(*courses)
        return s

    def update(self, instance, validated_data):
        print("vadata:", validated_data)
        year = validated_data.get('year')
        semester = validated_data.get('semester')
        course = validated_data.get('course')
        course = course.split(",")
        courses = Course.objects.filter(name__in=course)
        instance.year = year
        instance.semester = semester
        instance.course.set(courses)
        instance.save()
        return instance
    class Meta:
        model = Semester
        fields = '__all__'

class ClassSerializer(ModelSerializer):
    course = serializers.CharField()
    semester = serializers.CharField()
    lecturer = serializers.CharField()

    mycourse = serializers.SerializerMethodField(required=False)
    mysemester = serializers.SerializerMethodField(required=False)
    mylecturer = serializers.SerializerMethodField(required=False)
    # student = serializers.CharField()

    def get_mycourse(self, instance):
        try:
            cname = instance.course.name
            return cname
        except Exception as e:
            print(e)
            return ""

    def get_mysemester(self, instance):
        try:
            sname = instance.semester.semester
            return sname
        except Exception as e:
            print(e)
            return ""

    def get_mylecturer(self, obj):
        try:
            lname = obj.lecturer.user.first_name
            return lname
        except Exception as e:
            print(e)
            return ""

    def create(self, validated_data):
        print("vadata:", validated_data)
        number = validated_data.get('number')
        semester = validated_data.get('semester')
        course = validated_data.get('course')
        lecturer = validated_data.get('lecturer')
        # student = validated_data.get('student')
        # student = student.split(",")
        # print(f'Group:{student}')
        mycourse = Course.objects.get(name=course)
        mysemester = Semester.objects.get(semester=semester)
        mylecturer = Lecturer.objects.get(staff_id=lecturer)
        # s = Student.objects.filter(student_id__in=student)
        myclass = Class.objects.create(number=number, course=mycourse, lecturer=mylecturer, semester=mysemester)
        # myclass.student.add(*s)
        return myclass

    def update(self, instance, validated_data):
        print("vadata:", validated_data)
        number = validated_data.get('number')
        semester = validated_data.get('semester')
        course = validated_data.get('course')
        lecturer = validated_data.get('lecturer')


        mycourse = Course.objects.get(name=course)  # 获取课程对象
        mysemester = Semester.objects.get(semester=semester)
        mylecturer = Lecturer.objects.get(staff_id=lecturer)

        instance.number = number
        instance.semester = mysemester
        instance.course = mycourse
        instance.lecturer = mylecturer
        instance.save()
        return instance

    class Meta:
        model = Class
        fields = '__all__'

class StudentSerializer(ModelSerializer):
    mycourse = serializers.CharField()
    myclass = serializers.CharField()
    user = serializers.CharField()

    uname = serializers.SerializerMethodField(required=False)
    courses = serializers.SerializerMethodField(required=False)
    classes = serializers.SerializerMethodField(required=False)
    myemail = serializers.SerializerMethodField(required=False)

    def get_uname(self, obj):
        try:
            uname = obj.user.username
            return uname
        except Exception as e:
            print(e)
            return ""

    def get_courses(self, obj):
        cs = obj.mycourse.all()
        cstr = ""
        for c in cs:
            cstr += c.name
            cstr += " "
        return cstr

    def get_classes(self, obj):
        cs = obj.myclass.all()
        cstr = ""
        for c in cs:
            cstr += str(c.number)
            cstr += " "
        return cstr

    def get_myemail(self, obj):
        email = obj.user.email
        return email

    def create(self, validated_data):
        print("vadata:", validated_data)
        student_id = validated_data.get('student_id')
        DOB = validated_data.get('DOB')
        attend = validated_data.get('attend')
        myclass = validated_data.get('myclass')
        mycourse = validated_data.get('mycourse')
        user = validated_data.get('user')
        myuser = User.objects.get(username=user)
        mycourse = mycourse.split(',')
        myclass = myclass.split(',')
        # student = validated_data.get('student')
        # student = student.split(",")
        # print(f'Group:{student}')
        mycourse = Course.objects.filter(name__in=mycourse)
        myclass = Class.objects.filter(number__in=myclass)

        # s = Student.objects.filter(student_id__in=student)
        stu = Student.objects.create(student_id=student_id, DOB=DOB, attend=attend, user=myuser)
        stu.mycourse.add(*mycourse)
        stu.myclass.add(*myclass)
        # myclass.student.add(*s)
        return myclass

    def update(self, instance, validated_data):
        print("vadata:", validated_data)
        student_id = validated_data.get('student_id')
        DOB = validated_data.get('DOB')
        attend = validated_data.get('attend')
        myclass = validated_data.get('myclass')
        mycourse = validated_data.get('mycourse')
        user = validated_data.get('user')
        myuser = User.objects.get(username=user)
        mycourse = mycourse.split(',')
        myclass = myclass.split(',')
        mycourse = Course.objects.filter(name__in=mycourse)
        myclass = Class.objects.filter(number__in=myclass)

        instance.student_id = student_id
        instance.DOB = DOB
        instance.attend = attend
        instance.user = myuser
        instance.mycourse.set(mycourse)
        instance.myclass.set(myclass)
        instance.save()

        return instance

    class Meta:
        model = Student
        fields = '__all__'

class CollegeDaySerializer(ModelSerializer):

    class Meta:
        model = College_Day
        fields = '__all__'
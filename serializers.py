from rest_framework import serializers
from .models import StudentApp, StudentReg, Staff, Department
from django.contrib.auth.models import User


class StudentAppSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentApp
        fields = ["id", "student_name", "email", "ssc_memo", "inter_memo"]

        def create(self, validated_data):
            return StudentApp.objects.create(**validated_data)


class StudentRegSerializer(serializers.ModelSerializer):
    # password = serializers.CharField()

    class Meta:
        model = StudentReg
        fields = ["id", "student_apps", "student_name", "student_email", "student_father_name", "student_mother_name",
                  "student_mobile", "student_profile_photo", "department", "user"]

        def create(self, validated_data):
            return StudentReg.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.student_apps = validated_data.get('student_apps', instance.student_apps)
            instance.student_name = validated_data.get('student_name', instance.student_name)
            instance.student_email = validated_data.get('student_email', instance.student_email)
            instance.student_father_name = validated_data.get('student_father_name', instance.student_father_name)
            instance.student_mother_name = validated_data.get('student_mother_name', instance.student_mother_name)
            instance.student_mobile = validated_data.get('student_mobile', instance.student_mobile)
            instance.student_profile_photo = validated_data.get('student_profile_photo', instance.student_profile_photo)
            instance.department = validated_data.get('department', instance.department)
            # instance.user = validated_data.get('user', instance.user)
            instance.save()
            return instance


class StaffSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = Staff
        fields = ["id", "staff_name", "staff_email", "staff_father_name", "staff_mother_name",
                  "staff_profile_photo", "staff_mobile", "department", "user", "password"]

    def create(self, validated_data):
        return Staff.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.staff_name = validated_data.get('staff_name', instance.staff_name)
        instance.staff_email = validated_data.get('staff_email', instance.staff_email)
        instance.staff_father_name = validated_data.get('staff_father_name', instance.staff_father_name)
        instance.staff_mother_name = validated_data.get('staff_mother_name', instance.staff_mother_name)
        instance.staff_profile_photo = validated_data.get('staff_profile_photo', instance.staff_profile_photo)
        instance.staff_mobile = validated_data.get('staff_mobile', instance.staff_mobile)
        instance.department = validated_data.get('department', instance.department)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ["department_name"]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

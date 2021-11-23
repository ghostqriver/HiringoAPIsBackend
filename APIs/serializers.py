from rest_framework import serializers
from .models import UserStudentProfile,UserTeacherProfile,StudentBasic,TeacherBasic,CourseBasic,SubjectBasic
class StudentInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model=UserStudentProfile#指定序列化从哪个模型映射字段
        fields='__all__'#映射哪些字段

class TeacherInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model=UserTeacherProfile
        fields='__all__'

class StudentAccountSerializers(serializers.ModelSerializer):
    class Meta:
        model=StudentBasic
        fields='__all__'

class TeacherAccountSerializers(serializers.ModelSerializer):
    class Meta:
        model=TeacherBasic
        fields='__all__'

class CourseInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model=CourseBasic
        fields='__all__'

class SubjectInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model=SubjectBasic
        fields='__all__'
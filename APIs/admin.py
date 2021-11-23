from django.contrib import admin
from APIs.models import StudentBasic,TeacherBasic,CourseBasic,UserStudentProfile,UserTeacherProfile,SubjectBasic
# Register your models here.
admin.site.register(StudentBasic)
admin.site.register(TeacherBasic)
admin.site.register(CourseBasic)
admin.site.register(UserStudentProfile)
admin.site.register(UserTeacherProfile)
admin.site.register(SubjectBasic)


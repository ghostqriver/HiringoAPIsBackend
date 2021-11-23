from django.contrib import admin
from APIs.models import StudentBasic,TeacherBasic,CourseBasic,UserStudentProfile,UserTeacherProfile,SubjectBasic
# Register your models here.
admin.site.site_header = 'Hiringo Administration System'  # 设置header
admin.site.site_title = 'Hiringo'

admin.site.register(StudentBasic,)
admin.site.register(TeacherBasic)
admin.site.register(CourseBasic)
admin.site.register(UserStudentProfile)
admin.site.register(UserTeacherProfile)
admin.site.register(SubjectBasic)


from django.urls import path
from . import  views
from rest_framework.routers import DefaultRouter
urlpatterns = [
    path('',views.APIRootView.as_view())
    # #url of studentlist
    # path('students/',views.StudentListView.as_view()),
    # #url of studentdetail
    # path('students/<int:pk>', views.StudentDetailView.as_view())
]
router=DefaultRouter() #创建路由器
router.register(r'students',views.StudentInfoView) #注册路由
urlpatterns +=router.urls #把注册好的路由拼接到urlpatterns

router.register(r'teachers',views.TeacherInfoView)
urlpatterns +=router.urls

router.register(r'studentsaccount',views.StudentAccountView)
urlpatterns +=router.urls

router.register(r'teachersaccount',views.TeacherInfoView)
urlpatterns +=router.urls

router.register(r'courses',views.CourseInfoView)
urlpatterns +=router.urls

router.register(r'subjects',views.SubjectInfoView)
urlpatterns +=router.urls
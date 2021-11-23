from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('', views.APIRootView.as_view()),
    path('docs/', include_docs_urls(title='Hiringo API documentation')),
]
router = DefaultRouter()  # 创建路由器
router.register(r'students', views.StudentInfoView)  # 注册路由
urlpatterns += router.urls  # 把注册好的路由拼接到urlpatterns

router.register(r'teachers', views.TeacherInfoView)
urlpatterns += router.urls

router.register(r'studentsaccount', views.StudentAccountView)
urlpatterns += router.urls

router.register(r'teachersaccount', views.TeacherInfoView)
urlpatterns += router.urls

router.register(r'courses', views.CourseInfoView)
urlpatterns += router.urls

router.register(r'subjects', views.SubjectInfoView)
urlpatterns += router.urls

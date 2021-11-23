# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class StudentBasic(models.Model):
    student_name = models.AutoField(primary_key=True)
    student_email = models.CharField(max_length=255)
    student_password = models.CharField(max_length=255)
    is_superuser = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'student_basic'

    def __str__(self):
        return str(self.student_name)


class TeacherBasic(models.Model):
    teacher_name = models.AutoField(primary_key=True)
    teacher_email = models.CharField(max_length=255)
    teacher_password = models.CharField(max_length=255)
    is_superuser = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'teacher_basic'

    def __str__(self):
        return str(self.teacher_name)


class UserPermission(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    content = models.IntegerField()
    codename = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_permission'


class UserStudentProfile(models.Model):
    user = models.OneToOneField(StudentBasic, models.DO_NOTHING, primary_key=True)
    user_firstname = models.CharField(max_length=25, default='')
    user_secondname = models.CharField(max_length=25, default='')
    user_biography = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    user_telephone = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'user_student_profile'

    def __str__(self):
        return str(self.user)


class UserTeacherProfile(models.Model):
    user = models.OneToOneField(TeacherBasic, models.DO_NOTHING, primary_key=True)
    user_firstname = models.CharField(max_length=25, default='')
    user_secondname = models.CharField(max_length=25, default='')
    user_subject_type = models.ForeignKey('SubjectBasic', models.DO_NOTHING)
    user_biography = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    user_telephone = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'user_teacher_profile'
        unique_together = (('user', 'user_subject_type'),)

    def __str__(self):
        return str(self.user)


class CourseBasic(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('StudentBasic', models.DO_NOTHING)
    course_id = models.IntegerField()
    course_amount = models.IntegerField()
    course_payment_currecy = models.DateTimeField()
    course_status = models.IntegerField()
    course_teacher = models.ForeignKey('TeacherBasic', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'course_basic'
        unique_together = (('transaction_id', 'student'),)

    def __str__(self):
        return str(self.transaction_id)


class SubjectBasic(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'subject_basic'

    def __str__(self):
        return str(self.subject_name)

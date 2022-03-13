from django.contrib import admin

from .models import Student, Teacher


# class TeacherInline(admin.TabularInline):
#     model = Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    # inlines = [TeacherInline, ]

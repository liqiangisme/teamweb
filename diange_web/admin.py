from django.contrib import admin

# Register your models here.
from .models import Grade,Student
#注册
class GradeAdmin(admin.ModelAdmin):
    #列表属性页
    list_display = ['pk','gname','gdata']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5
    #添加修改属性页
    fields = ['gdata','pk','gname']

class StudentAdmin(admin.ModelAdmin):
    #列表属性页
    list_display = ['pk','sname','sage','sgrade']
    list_filter = ['sname']
    search_fields = ['sname']
    list_per_page = 5
    #添加修改属性页
    fieldsets = [("one",{"fields":['sname']}),("two",{"fields":['sage','sgrade']})]


admin.site.register(Grade,GradeAdmin)
admin.site.register(Student,StudentAdmin)
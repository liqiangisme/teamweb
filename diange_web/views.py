from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #return render(request,'index.html')
    return HttpResponse("liqiang is a good man")
def detail(request,num):
    return HttpResponse("detail-%s"%num)

from .models import Grade,Student
def gra(request):
    #去模板里取数据
    graList = Grade.objects.all()
    #将数据传递给模板，模板再渲染页面，将渲染好的页面返回给浏览器
    return render(request,'grade.html',{"grade":graList})

def stu(request):
    #去模板里取数据
    stuList = Student.objects.all()
    #将数据传递给模板，模板再渲染页面，将渲染好的页面返回给浏览器
    return render(request,'student.html',{"student":stuList})

def gradeStudent(request,num):
    gra = Grade.objects.get(pk=num)
    stuList = gra.student_set.all()
    return render(request,'student.html',{"student":stuList})

def member(request):
    gra = Grade.objects.get(pk=num)
    stuList = gra.student_set.all()
    return render(request, 'member.html', {"student": stuList})

def home(request):
    # 去模板里取数据
    graList = Grade.objects.all()
    # 将数据传递给模板，模板再渲染页面，将渲染好的页面返回给浏览器
    return render(request, 'home.html', {"grade": graList})
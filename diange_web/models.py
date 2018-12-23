from django.db import models

# Create your models here.

class Grade(models.Model):
    gname = models.CharField(max_length=20)
    gdata = models.DateField()
    def __str__(self):
        return "%s"%(self.gname)

class Student(models.Model):
    sname = models.CharField(max_length=20)
    sage = models.IntegerField()
    sgrade = models.ForeignKey("Grade",on_delete=models.CASCADE)
    def __str__(self):
        return "%s-%d"%(self.sname,self.sage)

#不需要定义主键
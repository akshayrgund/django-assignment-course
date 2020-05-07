from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Course,Student,course_enrolment

def index(request):
    return HttpResponse("this is courseIndex")

def totalstudents(request,course_id):

    ceList = course_enrolment.objects.filter(course = course_id)
    output = '';
    for ce in ceList:
        output = output +'\n'+ce.student.name;


    return HttpResponse(output);

def enroll(request,course_id,student_id):
    c = Course.objects.filter(id = course_id)[0];
    s = Student.objects.filter(id = student_id)[0];
    ce = course_enrolment(course = c,student = s)
    ce.save();
    return HttpResponse('Enrolled')
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .api_login import api_login_template, api_signup_template
from .api_leave import api_student_leave
from .api_complain import api_student_complaint
from .api_room import api_student_room
from .api_mess import api_student_mess
from .api_course import (
    api_course_getall,
    api_student_getregistered,
    api_student_addcourse,
)


# Create your views here.
@csrf_exempt
def index(request):
    template = loader.get_template("core/index.html")
    return HttpResponse(template.render())


@csrf_exempt
def student_login(request):
    api_url = "http://localhost:8000/api/v1/student/auth/login"
    return api_login_template(api_url, request)


@csrf_exempt
def warden_login(request):
    api_url = "http://localhost:8000/api/v1/warden/auth/login"
    return api_login_template(api_url, request)


@csrf_exempt
def faculty_login(request):
    api_url = "http://localhost:8000/api/v1/faculty/auth/login"
    return api_login_template(api_url, request)


@csrf_exempt
def student_signup(request):
    api_url = "http://localhost:8000/api/v1/student/auth/register"
    return api_signup_template(api_url, request)


@csrf_exempt
def faculty_signup(request):
    api_url = "http://localhost:8000/api/v1/faculty/auth/register"
    return api_signup_template(api_url, request)


@csrf_exempt
def student_dashboard(request):
    template = loader.get_template("core/student_dashboard.html")
    return HttpResponse(template.render())


@csrf_exempt
def faculty_dashboard(request):
    template = loader.get_template("core/faculty_dashboard.html")
    return HttpResponse(template.render())


@csrf_exempt
def warden_dashboard(request):
    template = loader.get_template("core/warden_dashboard.html")
    return HttpResponse(template.render())


@csrf_exempt
def student_leave(request):
    return api_student_leave(request)


@csrf_exempt
def student_complaint(request):
    return api_student_complaint(request)


@csrf_exempt
def student_room(request):
    return api_student_room(request)


@csrf_exempt
def student_mess(request):
    return api_student_mess(request)


@csrf_exempt
def course_getall(request):
    return api_course_getall(request)


@csrf_exempt
def student_getregistered(request):
    return api_student_getregistered(request)


@csrf_exempt
def student_addcourse(request):
    return api_student_addcourse(request)

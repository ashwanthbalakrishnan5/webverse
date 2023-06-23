import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def api_course_getall(request):
    api_url = "http://localhost:8000/api/v1/student/get-all"
    jwt = request.session.get("jwt")
    if request.method == "GET":
        headers = {"Authorization": f"Bearer {jwt}"}
        try:
            response = requests.get(api_url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                return HttpResponse(data)
            else:
                error_message = "API Error: " + response.json().get("errors")
                return HttpResponse(error_message)
        except requests.exceptions.RequestException as e:
            error_message = str(e)
            return HttpResponse(error_message)
    else:
        return HttpResponse("Method not allowed", status=405)


def api_student_getregistered(request):
    api_url = "http://localhost:8000/api/v1/student/get-all-registered"
    jwt = request.session.get("jwt")
    if request.method == "GET":
        headers = {"Authorization": f"Bearer {jwt}"}
        try:
            response = requests.get(api_url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                return HttpResponse(data)
            else:
                error_message = "API Error: " + response.json().get("errors")
                return HttpResponse("error")
        except requests.exceptions.RequestException as e:
            error_message = str(e)
            return HttpResponse("error")
    else:
        return HttpResponse("error", status=405)


def api_student_addcourse(request):
    api_url = "http://localhost:8000/api/v1/student/course/add-course"
    jwt = request.session.get("jwt")
    if request.method == "POST":
        headers = {"Authorization": f"Bearer {jwt}"}
        form_data = request.POST.dict()
        headers = {"Content-Type": "application/json"}
        try:
            response = requests.post(api_url, json=form_data, headers=headers)
            if response.status_code == 201:
                return HttpResponse("Success!")
            else:
                error_message = "API Error: " + response.json().get("errors")
                return HttpResponse(error_message)
        except requests.exceptions.RequestException as e:
            error_message = str(e)
            return HttpResponse(error_message)

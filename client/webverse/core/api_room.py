import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def api_student_room(request):
    api_url = "http://localhost:8000/api/v1/student/room-details"
    jwt = request.session.get("jwt")
    if request.method == "GET":
        headers = {"Authorization": f"Bearer {jwt}"}
        try:
            response = requests.get(api_url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                return HttpResponse(render({"data": data}))
            else:
                error_message = "API Error: " + response.json().get("errors")
                return HttpResponse(render({"error_message": error_message}))
        except requests.exceptions.RequestException as e:
            error_message = str(e)
            return HttpResponse(render({"error_message": error_message}))
    else:
        return HttpResponse(render({"message": "Method not allowed"}), status=405)


def api_warden_room(request):
    api_url = "http://localhost:8000/api/v1/warden/room-details"
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


def api_warden_room_create(request):
    api_url = "http://localhost:8000/api/v1/warden/room-details/create"
    jwt = request.session.get("jwt")
    if request.method == "POST":
        form_data = request.POST.dict()
        headers = {"Content-Type": "application/json"}
        try:
            response = requests.post(api_url, json=form_data, headers=headers)
            if response.status_code == 200:
                return HttpResponse("Success!")
            else:
                error_message = "API Error: " + response.json().get("errors")
                return HttpResponse(error_message)
        except requests.exceptions.RequestException as e:
            error_message = str(e)
            return HttpResponse(error_message)
    else:
        return HttpResponse("message", status=405)


def api_warden_nastudent(request):
    api_url = (
        "http://localhost:8000/api/v1/warden/room-details/getALLNotAssignedStudents"
    )
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


def api_warden_naroom(request):
    api_url = "http://localhost:8000/api/v1/warden/room-details/getALLNotAssignedRooms"
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

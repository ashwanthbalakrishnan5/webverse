import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def api_student_mess(request):
    api_url = "http://localhost:8000/api/v1/student/mess-details"
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
    if request.method == "PUT":
        form_data = request.POST.dict()
        headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}
        try:
            response = requests.put(api_url, json=form_data, headers=headers)
            if response.status_code == 200:
                return HttpResponse(render({"message": "Success!"}))
            else:
                error_message = "API Error: " + response.json().get("errors")
                return HttpResponse(render({"error_message": error_message}))
        except requests.exceptions.RequestException as e:
            error_message = str(e)
            return HttpResponse(render({"error_message": error_message}))
    else:
        return HttpResponse(render({"message": "Method not allowed"}), status=405)

import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json


def api_login_template(api_url, request):
    if request.method == "POST":
        form_data = json.loads(request.body)

        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(api_url, json=form_data, headers=headers)

            if response.status_code == 200:
                jwt = response.json().get("token")
                request.session["jwt"] = jwt
                print("JWT: ", jwt)
                # template = loader.get_template("core/index.html")
                # return HttpResponse(template.render())
                # return HttpResponse("Success!")
            else:
                error_message = response.json()
                # error_template = loader.get_template("error.html")
                return HttpResponse(error_message)
        except requests.exceptions.RequestException as e:
            error_message = str(e)
            # error_template = loader.get_template("error.html")
            return HttpResponse(error_message)
    elif request.method == "OPTIONS":
        # Handle OPTIONS request
        # Add appropriate headers to allow the desired methods and origins
        response = HttpResponse()
        response[
            "Access-Control-Allow-Origin"
        ] = "http://localhost:5500"  # Replace with your desired origin
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response[
            "Access-Control-Max-Age"
        ] = "86400"  # Specify the maximum age of preflight request cache
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response
    else:
        # return method not allowed error with 405 status code
        printf("Method not allowed here")
        return HttpResponse(render({"message": "Method not allowed"}), status=405)


def api_signup_template(api_url, request):
    if request.method == "POST":
        # form_data = request.POST.dict()
        form_data = json.loads(request.body)

        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(api_url, json=form_data, headers=headers)
            if response.status_code == 201:
                # success_template = loader.get_template('success.html')
                return HttpResponse("Success!")
            else:
                error_message = response.json().get("errors")
                # error_template = loader.get_template("error.html")
                return HttpResponse(error_message)
        except requests.exceptions.RequestException as e:
            error_message = str(e)
            # error_template = loader.get_template("error.html")
            return HttpResponse(error_message)
    elif request.method == "OPTIONS":
        # Handle OPTIONS request
        # Add appropriate headers to allow the desired methods and origins
        response = HttpResponse()
        response[
            "Access-Control-Allow-Origin"
        ] = "http://localhost:5500"  # Replace with your desired origin
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response[
            "Access-Control-Max-Age"
        ] = "86400"  # Specify the maximum age of preflight request cache
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response
    else:
        # return method not allowed error with 405 status code
        return HttpResponse("message", status=405)

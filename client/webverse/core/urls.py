from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("student/login", views.student_login, name="student_login"),
    path("warden/login", views.warden_login, name="warden_login"),
    path("faculty/login", views.faculty_login, name="faculty_login"),
    path("student/signup", views.student_signup, name="student_signup"),
    path("faculty/signup", views.faculty_signup, name="faculty_signup"),
    path("student/dashboard", views.student_dashboard, name="student_dashboard"),
    path("faculty/dashboard", views.faculty_dashboard, name="faculty_dashboard"),
    path("warden/dashboard", views.warden_dashboard, name="warden_dashboard"),
    path("student/leave", views.student_leave, name="student_leave"),
    path("student/complaint", views.student_complaint, name="student_complaint"),
    path("student/room", views.student_room, name="student_room"),
    path("student/mess", views.student_mess, name="student_mess"),
    path("student/course", views.course_getall, name="course_getall"),
    path(
        "student/registered", views.student_getregistered, name="student_getregistered"
    ),
    path("student/addcourse", views.student_addcourse, name="student_addcourse"),
]

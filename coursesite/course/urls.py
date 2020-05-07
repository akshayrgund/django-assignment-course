from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:course_id>/totalstudents',views.totalstudents,name='totalstudents'),
    path('<int:course_id>/<int:student_id>/enroll', views.enroll, name='enroll'),
]
from django.urls import path
from . import views
from .api import StudentAppView, StudentRegView, StaffView, DepartmentView

app_name = 'college'
urlpatterns = [
    # path('', views.index_view, name='index'),
    # path('application/', views.application, name='application'),
    # path('student_registration/', views.student_registration, name='student-registration'),
    # path('staff_registration/', views.staff_registration, name='staff-registration'),
    # path('login/', views.login_view, name='login'),
    # path('details/', views.details, name='details'),
    # path('student_staff_list/', views.student_staff_list, name='student-staff-list'),
    # path('student_app/', StudentAppView.as_view()),
    # path('student_reg/', StudentRegView.as_view()),
    # path('staff/', StaffView.as_view()),

    path('studentapp/', StudentAppView.as_view()),
    path('studentreg/', StudentRegView.as_view()),
    path('studentreg/<int:pk>/', StudentRegView.as_view()),
    path('department/', DepartmentView.as_view()),
    path('staff/', StaffView.as_view()),
    path('staff/<int:pk>/', StaffView.as_view()),
]
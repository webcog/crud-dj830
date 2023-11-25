from django.urls import path
from core import views

urlpatterns = [
   path("",views.index, name="index"),
   path('viewstudent/', views.viewSudent, name='viewStudent'),
   path('update/<int:pk>', views.update_student, name='update')
]
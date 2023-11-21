from django.shortcuts import render
from core.models import Student
# Create your views here.

def index(request):
    return render(request, 'index.html')


def viewSudent(request):

    student = Student.objects.all()

    context = {
        'student':student,
        }


    return render(request, 'viewstudent.html', context)
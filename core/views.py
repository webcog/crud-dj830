from django.shortcuts import render, redirect
from core.models import Student
# Create your views here.

def index(request):
    
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        father_name = request.POST.get('fathername')
        email = request.POST.get('email')
        addressOne = request.POST.get('inputAddressOne')
        addressTwo = request.POST.get('inputAddressTwo')
        cnic = request.POST.get('cnic')
        contact = request.POST.get('contact')

        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            father_name=father_name,
            email=email,
            addressOne=addressOne,
            addressTwo=addressTwo,
            cnic=cnic,
            contact=contact
        )
        return redirect('viewStudent')



    return render(request, 'index.html')


def viewSudent(request):

    student = Student.objects.all()

    context = {
        'student':student,
        }


    return render(request, 'viewstudent.html', context)
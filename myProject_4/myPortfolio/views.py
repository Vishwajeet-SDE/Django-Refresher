from django.shortcuts import render
from myPortfolio.models import Student

# Create your views here.

def student_list(request):
    students = Student.objects.filter(is_active=True).order_by('first_name', 'last_name')
    return render(request, 'portfolio/student_list.html', {'students': students})
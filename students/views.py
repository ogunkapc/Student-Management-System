from django.shortcuts import render
from .models import Student

# Create your views here.


def index(request):
    # Home page
    return render(request, 'students/index.html', {
        'students': Student.objects.all()
    })



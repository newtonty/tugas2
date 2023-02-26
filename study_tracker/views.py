from django.shortcuts import render

from .models import Assignment

def index(request):
    assignments = Assignment.objects.all()
    context = {
        'list_of_assignments' : assignments,
    }
    return render(request, 'tracker.html', context)
from django.shortcuts import render
from mood.forms import WellbeingForm
# Create your views here.

def index(request):
    context = {}
    context['form'] = WellbeingForm()
    return render(request, 'mood/index.html', context)
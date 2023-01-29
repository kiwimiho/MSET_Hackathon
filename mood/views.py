from django.shortcuts import render
from mood.forms import WellbeingForm
from mood.models import WellBeing
from django.http import HttpResponseRedirect
# Create your views here.

# from django import template
  
# register = template.Library()

# moodDict = {
#     'ecstatic':1,
#     'excited':2,
#     'happy':3,
#     'confident':4,
#     'inspired':5,
#     'calm':6,
#     'tired':7,
#     'sad':8,
#     'stressed':9,
#     'scared':10,
#     'depressed':11,
#     'angry':12,
# }

# @register.filter
# def mood_filter(value):
#     return moodDict[value]

def index(request):
    context = {}
    context['form'] = WellbeingForm()
    return render(request, 'mood/index.html', context)


def user_mood(request):
    form = WellbeingForm(request.POST)

    if request.method == 'POST':
        wellbeing_form = WellbeingForm(data=request.POST)

        if wellbeing_form.is_valid():

            # grab user_form and save to the DB
            choice = wellbeing_form.save()
            choice.save()
    return HttpResponseRedirect('/mood/show_mood')

def show_mood(request):
    mood_list = WellBeing.objects.order_by('date')
    mood_dict = {'moods': mood_list}
    return render(request, 'mood/showmood.html',context=mood_dict)


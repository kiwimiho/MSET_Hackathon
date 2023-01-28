from django.shortcuts import render
from mood.forms import WellbeingForm
from mood.models import WellBeing
from django.http import HttpResponseRedirect
# Create your views here.

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
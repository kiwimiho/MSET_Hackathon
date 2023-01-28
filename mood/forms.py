from django import forms
from mood.models import WellBeing

MOODS = (
    ('ecstatic', 'ecstatic'),
    ('excited', 'excited'),
    ('happy', 'happy'),
    ('confident', 'confident'),
    ('inspired', 'inspired'),
    ('calm', 'calm'),
    ('tired', 'tired'),
    ('sad', 'sad'),
    ('stressed', 'stressed'),
    ('scared', 'scared'),
    ('depressed', 'depressed'),
    ('angry', 'angry'),
)
ACTIVITIES = (
    ('exam', 'exam'),
    ('performance', 'performance'),
    ('exercise', 'exercise'),
    ('eating', 'eating'),
    ('hanging out with friends', 'hanging out with friends'),
    ('a meeting', 'a meeting'),
    ('after school practice', 'after school practice'),
    ('homework', 'homework'),
    ('classes', 'classes'),
    ('going outside', 'going outside'),
    ('vacation', 'vacation'),
    ('extracurriculars', 'extracurriculars'),
    ('working', 'working'),
    ('entertainment', 'entertainment'),
    ('napping', 'napping'),
)

class WellbeingForm(forms.ModelForm):
    mood = forms.ChoiceField(choices=MOODS,widget=forms.RadioSelect)
    activity = forms.ChoiceField(choices=ACTIVITIES,widget=forms.RadioSelect)
    class Meta():
        model = WellBeing
        fields = ('date', 'mood', 'activity')
from django import template
  
register = template.Library()

moodDict = {
    'ecstatic':5,
    'excited':4,
    'happy':3,
    'confident':2,
    'inspired':1,
    'calm':0,
    'tired':-1,
    'sad':-2,
    'stressed':-3,
    'scared':-4,
    'depressed':-5,
    'angry':-6,
}

@register.filter
def mood_filter(value):
    return moodDict[value]
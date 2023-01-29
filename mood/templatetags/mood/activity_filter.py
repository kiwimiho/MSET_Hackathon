from django import template
  
register = template.Library()

activityDict = {
    'exam':5,
    'performance':4,
    'exercise':3,
    'eating':2,
    'hanging out with friends':1,
    'a meeting':0,
    'after school practice':-1,
    'homework':-2,
    'classes':-3,
    'going outside':-4,
    'vacation':-5,
    'extracurriculars': -6,
    'working':-7,
    'entertainment':-8,
    'napping':-9,
}

@register.filter
def activity_filter(value):
    return activityDict[value]
from django import template
  
register = template.Library()

moodColorDict = {
    'ecstatic':'lightblue',
    'excited':'lightblue',
    'happy':'lightblue',
    'confident':'lightblue',
    'inspired':'lightblue',
    'calm':'lightblue',
    'tired':'lightpink',
    'sad':'lightpink',
    'stressed':'lightpink',
    'scared':'lightpink',
    'depressed':'lightpink',
    'angry':'lightpink',
}

@register.filter
def moodcolor_filter(value):
    return moodColorDict[value]
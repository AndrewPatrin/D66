from django import template
import re

register = template.Library()

@register.filter()
def censor(text):
    wordstocensor = ['fool', 'death', 'suffer']
    text = re.split('(\W+)', text)
    for i, j in enumerate(text):
        for k in wordstocensor:
            if k in j.lower():
                text[i] = text[i][0] + '*'*(len(text[i]) - 1)
    return ''.join(text)
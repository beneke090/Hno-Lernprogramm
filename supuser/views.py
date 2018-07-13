from django.http import HttpResponse
from django.template.loader import get_template
from lernen.models import Artikel


def supauser(request):
    t = get_template('supauser.html')
    html = t.render()
    return HttpResponse(html)

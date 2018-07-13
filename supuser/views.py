from django.http import HttpResponse
from django.template.loader import get_template
from lernen.models import Artikel
from supuser.forms import ArtikelForm


def supauser(request):
    f = ArtikelForm()
    t = get_template('supauser.html')
    c = {}
    if request.user.is_authenticated():
        c = {"form": f}
        c["logged_in"] = True
    html = t.render(c)
    return HttpResponse(html)


def newarticle(request):
    f = ArtikelForm()
    t = get_template('newarticle.html')
    if request.user.is_authenticated():
        c = {"form": f}
        c["logged_in"] = True
    html = t.render(c)
    return HttpResponse(html)

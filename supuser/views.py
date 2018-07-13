from django.http import HttpResponse
from django.template.loader import get_template
from lernen.models import Artikel
from supuser.forms import ArtikelForm


def supauser(request):
    f = ArtikelForm()
    t = get_template('supauser.html')
    if request.user.is_authenticated():
        html = t.render({"test": "test", "form": f})
    else:
        html = t.render({"test": "falsch", "form": f})
    return HttpResponse(html)

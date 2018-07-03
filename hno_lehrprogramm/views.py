from django.http import HttpResponse
from django.template.loader import get_template
from lernen.models import Artikel

def start(request):
    ersteSeite = Artikel.objects.get(my_order=1).title
    t = get_template('start.html')
    html = t.render({"ersteSeite": ersteSeite})
    return HttpResponse(html)

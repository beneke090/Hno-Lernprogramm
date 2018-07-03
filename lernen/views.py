from django.http import HttpResponse
from django.template import loader
from lernen.models import Artikel
from lernen.models import Kapitel

def article(request):
    t = loader.get_template('lernseite.html')
    if request.path == "/lernen/":
        art = Artikel.objects.get(my_order=1)
    else:
        art =Artikel.objects.get(title=request.path.split("/")[2])
    active = str(art.kapitel)
    activetitle = str(art.title)

    """ Kapitel fuer Kapiteluebersicht suchen """
    kapitelliste= []
    linkliste=[]
    samekapitelarticle = []
    for article in Artikel.objects.all():
        if str(article.kapitel) not in kapitelliste:
            kapitelliste.append(str(article.kapitel))
            linkliste.append("/lernen/"+str(article.title))
        if str(article.kapitel) == str(art.kapitel):
            samekapitelarticle.append(article.title)
    #[i.kapitelname for i in Kapitel.objects.all()]
    c = {"art": art,
        "kapitelliste": zip(kapitelliste,linkliste),
        "samekapitelarticle": zip(samekapitelarticle, ["/lernen/" + art.replace(" ","%20") for art in samekapitelarticle]),
        "active": active,
        "activetitle": activetitle}

    """ Bilder fuer Bilder suchen """
    imglist = []
    for img in art.artikelimages_set.all():
        print(img.image)
        imglist.append( img.image )
    if imglist != []:
        c["imglist"] = imglist

    """ Youtube Video einfuegen """
    if art.video != None:
        c["videolink"] = art.video


    try:
        naechst = Artikel.objects.get(my_order = art.my_order+1).title
        c["naechst"] = "/lernen/"+naechst
    except:
        pass
    try:
        zuruck = Artikel.objects.get(my_order = art.my_order-1).title
        c["zuruck"] = "/lernen/"+zuruck
    except:
        pass
    html = t.render(c)
    html = html.replace("(u)",'<u>')
    html = html.replace("(br)","<br>")
    html = html.replace("(/u)",'</u>')
    html = html.replace("(b)",'<b>')
    html = html.replace("(/b)",'</b>')
    html = html.replace("(***)",'<a href="#" data-toggle="popover" data-content="')
    html = html.replace("(**)",'" data-trigger="hover" data-placement="top">')
    html = html.replace("(*)",'</a>')

    return HttpResponse(html)

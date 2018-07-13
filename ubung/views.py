from django.http import HttpResponse
from django.template.loader import get_template
from ubung.models import Question, Answer
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from django import forms


def showbild(request):
    polygon = Polygon([(82, 22), (80, 80), (127, 147), (142, 63), (127, 14), (65, 16)])
    print(polygon)
    answer = False
    if request.method == "GET":
        #x,y = request.GET.lists
        # print(request.GET.urlencode())
        if bool(request.GET.dict()):
            x, y = request.META["QUERY_STRING"].split(",")
            point = Point(int(x), int(y))
            print(point)
            answer = True
            click = polygon.contains(point)
    t = get_template('bildtest.html')

    if answer:
        if click:
            html = t.render({"coordinates": str(x) + ", " + str(y), "answer": "richtig"})
        else:
            html = t.render({"coordinates": str(x) + ", " + str(y), "answer": "Falsch"})
    else:
        html = t.render()

    return HttpResponse(html)


def ubungTest(request):

    t = get_template("ubung.html")
    if request.path == "/ubung/":
        q = Question.objects.get(my_order=1)
    else:
        q = Question.objects.get(uberschrift=request.path.split("/")[2])

    active = str(q.kapitel)
    kapitelliste = []
    linkliste = []
    for ubung in Question.objects.all():
        if str(ubung.kapitel) not in kapitelliste:
            kapitelliste.append(str(ubung.kapitel))
            linkliste.append("/ubung/"+str(ubung.uberschrift))

    c = {"question": q,
         "kapitelliste": zip(kapitelliste, linkliste),
         "active": active,
         }
    try:
        naechst = Question.objects.get(my_order=q.my_order+1).uberschrift
        c["naechst"] = "/ubung/"+naechst
    except:
        pass
    try:
        zuruck = Question.objects.get(my_order=q.my_order-1).uberschrift
        c["zuruck"] = "/ubung/"+zuruck
    except:
        pass

    gleich = q.uberschrift
    c["gleich"] = gleich
    if len(q.answer_set.all()) != 0:
        answers = {}
        answernumm = []
        i = 0
        for answer in q.answer_set.all():
            i = i+1
            answers[str(answer.answer)] = answer.richtig
            answernumm.append(i)

        answerlist = answers.keys()
        if len(q.answer_set.filter(richtig=True)) < 2:
            c["singlechoice"] = "singlechoice"
        c["answerlist"] = answerlist
    elif q.coordinates != "":
        if request.method == "GET":
            if bool(request.GET.dict()):
                x, y = request.META["QUERY_STRING"].split(",")
                point = Point(int(x), int(y))
                polygonstr = q.coordinates
                polylist = []
                for coord in polygonstr.split(";"):
                    polylist.append((int(coord.split(",")[0]), int(coord.split(",")[1])))
                poly = Polygon(polylist)
                print(point)
                clicked = True
                clickrichtig = poly.contains(point)

                context["clicked"] = clicked
                context["clickrichtig"] = clickrichtig

        bildTestPath = "ubung/"+q.image
        c["bildTestPath"] = bildTestPath
    if request.user.is_authenticated():
        c["logged_in"] = True
    print(request.GET.getlist("choice"))
    try:
        givennum = []
        givenanswer = request.GET.getlist("choice")
        print(givenanswer)
        if givenanswer != []:
            richtigListe = []
            print(list(answers.values()))
            for i in range(len(list(answers.values()))):
                if list(answers.values())[i] == True and "choice"+str(i+1) in givenanswer:
                    richtigListe.append(True)
                elif list(answers.values())[i] == False and "choice"+str(i+1) not in givenanswer:
                    richtigListe.append(True)
                else:
                    richtigListe.append(False)

            print(richtigListe)
            c["richtig"] = not False in richtigListe
            c["falsch"] = False in richtigListe
        else:
            print("emppy")
            pass

    except:
        print("not woriking")
        pass
        # class UserForm(forms.Form):
        #     widget = forms.RadioSelect(answerneu)
        # form = UserForm
        # context["form"] = form
    html = t.render(c)
    return HttpResponse(html)

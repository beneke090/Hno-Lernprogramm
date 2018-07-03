from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Bild, Question, Answer, UbungKapitel



class ChoiceInline(admin.StackedInline):
    model = Answer
    extra=0

#class QuestionAdmin(admin.ModelAdmin):
#    fields = ["kapitel", "uberschrift", "text" ]
#    inlines = [ChoiceInline]



@admin.register(Question)
class QuestionAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display =('uberschrift','kapitel')
    inlines = [ChoiceInline]
    fields = ["kapitel", "uberschrift", "text", "frage", "image", "coordinates" ]

admin.site.register(Bild)
admin.site.register(UbungKapitel)
#admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)

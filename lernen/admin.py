from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Kapitel, Artikel, ArtikelImages

class ChoiceInline(admin.StackedInline):
    model = ArtikelImages
    extra=0

class ArtikelAdmin(admin.ModelAdmin):
    list_display =('title','kapitel')

admin.site.register(Kapitel)
#admin.site.register(Artikel, ArtikelAdmin)
#python manage.py reorder lernen.Artikel
@admin.register(Artikel)
class ArtikelAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display =('title','kapitel')
    inlines = [ChoiceInline]

admin.site.register(ArtikelImages)

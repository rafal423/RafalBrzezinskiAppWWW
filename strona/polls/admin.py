from django.contrib import admin

from .models import Osoba, Druzyna

class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'get_miesiac_urodzenia', 'get_druzyna']
    list_filter = ["druzyna"]

    def get_miesiac_urodzenia(self, obj):
        return obj.miesiac_urodzenia
    get_miesiac_urodzenia.short_description = "Miesiąc urodzenia"

    def get_druzyna(self, obj):
        return obj.druzyna
    get_druzyna.short_description = "Drużyna"

class DruzynaAdmin(admin.ModelAdmin):
    list_display = ["nazwa", "kraj"]
    list_filter = ["kraj"]


admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Druzyna, DruzynaAdmin)

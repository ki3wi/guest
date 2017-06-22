from django.contrib import admin
from sign.models import Event ,Guest


#admin.site.register(Event)
#admin.site.register(Guest)


class EventAdmin(admin.ModelAdmin):
    list_display = ['name','status','start_time','id']
    search_fields = ['name']
    list_filter = ['status']

admin.site.register(Event,EventAdmin)


class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname','phone','email','sign','event','creat_time']
    search_fields = ['realname','phone']
    list_filter = ['sign']
admin.site.register(Guest,GuestAdmin)
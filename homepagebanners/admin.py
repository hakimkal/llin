from django.contrib import admin

from .models import Homepagebanner

class BannerInline(admin.StackedInline):
    model = Homepagebanner
    
class HomepagebannerAdmin(admin.ModelAdmin):
    #list_display = ('image',)
    #inlines= [BannerInline];
    class Meta:
        verbose_name ='HomePage Banner'
    
    exclude = ('user',)
    
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()
    
admin.site.register(Homepagebanner, HomepagebannerAdmin)
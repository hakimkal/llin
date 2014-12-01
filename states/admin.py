from django.contrib import admin
from image_cropping import ImageCroppingMixin
from states.models import State
from states_documents.models import StateDocument

class BookInline(admin.TabularInline):
    model = StateDocument
class StateAdmin(ImageCroppingMixin,admin.ModelAdmin):
    list_display=('maps','name')
    inlines = [BookInline]
        

admin.site.register(State,StateAdmin)
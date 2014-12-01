from django.contrib import admin
from states.models import State
from states_documents.models import StateDocument


class StateDocumentAdmin(admin.ModelAdmin):
    list_display = ('filename', 'filepath','state','created','modified')
    

admin.site.register(StateDocument, StateDocumentAdmin)
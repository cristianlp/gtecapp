from django.contrib import admin
from django.contrib.auth.models import User, Group
from instrumentos.models import Instrumento, Organismo, Convocatoria
from empresas.models import Ciudad, Empresa, Visita
from integrantes.models import Integrante

@admin.register(Convocatoria)
class ConvocatoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'instrumento', 'hasta', 'monto_maximo',)
    list_filter = ('es_anr',)
    search_fields = ('nombre', 'instrumento__nombre', )



admin.site.register(Organismo)
admin.site.register(Instrumento)
admin.site.register(Ciudad)
admin.site.register(Empresa)
admin.site.register(Visita)
admin.site.register(Integrante)

admin.site.unregister(User)
admin.site.unregister(Group)

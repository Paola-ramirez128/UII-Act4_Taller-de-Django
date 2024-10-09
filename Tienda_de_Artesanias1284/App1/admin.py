from django.contrib import admin
from .models import Provedores, Sucursal

# Register your models here.
admin.site.site_header = "Hola"
admin.site.index_title = "Hola2"
admin.site.site_title = "Hola3"

class ProvedorAdmin(admin.ModelAdmin):
    fields = ["id_provedor", "telefono", "gmail", "raiting", "registro_fehca", "tipo", "provincia"]
    list_display = ["id_provedor", "telefono"]

def actualizar_o(self, request, queryset):
    for i in queryset:
        if "O" in object:
            id_provedor1 = object
            object.id_provedor = id_provedor1.replace("O", "o")
            object.save()

    self.message_user(request, "Exitosamente")
actualizar_o.short_description = "Actualizar letras O"
actions = ["actualizar_o"]

admin.site.register(Provedores, ProvedorAdmin)

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    fields = ["id_sucursal", "direccion", "ciudad", "nombre", "encargado", "telefono", "horario", "provedores_fk"]
    list_display = ["id_sucursal", "nombre"]
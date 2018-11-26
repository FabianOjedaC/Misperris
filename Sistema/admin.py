from django.contrib import admin

# Register your models here.
class AdminUsuario(admin.ModelAdmin):
    list_display = ["nombrePersona", "numeroFono"]
    class Meta:
        model = Persona


admin.site.register(Persona, AdminUsuario)

class AdminMascota(admin.ModelAdmin):
    list_display = ["nombreMascota", "estadoMascota"]
    class Meta:
        model = Mascota


admin.site.register(Mascota, AdminMascota)

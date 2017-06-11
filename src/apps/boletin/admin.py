from django.contrib import admin
from .models import Registrado
from .forms import RegModelForm
# Register your models here.
class AdminRegistrado(admin.ModelAdmin):
    list_display = ["email", "nombre","timestamp"] #que campos mostrar en el formulario
    form = RegModelForm #atender aca.. de donde estira
    #list_display_links = ["nombre"] #este sirve para cambiar el link de un atributo
    list_filter = ["timestamp"]
    #list_editable =["nombre"] #no se puede cambiar el email si es que es el link tambien
    search_fields = ["email","nombre"]
    # class Meta:
    #     model = Registrado
admin.site.register(Registrado, AdminRegistrado)

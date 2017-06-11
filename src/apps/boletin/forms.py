from django import forms
from .models import Registrado

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ["nombre","email"]
        #validaciones personalizadas... ejemplo
    def clean_email(self):
        email=self.cleaned_data.get("email")

        # Hacer validaciones propias por ejemplo para que solo guarde email con @yo.edu.com

        # email_base,proveedor = email.split("@") 
        # dominio,extension = proveedor.split(".")
        
        # if not extension == "edu":
        #     raise forms.ValidationError("Utilize un correo .EDU")
        return email
    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        #validaciones y return nombre
        return nombre

class ContactForm(forms.Form):
    # class Meta:
    #     model = Contact
    #     fields = ["nombre","email","mensaje"]
    # def clean_nombre(self):
    #     nombre = self.cleaned_data.get("nombre")
    #     return nombre
    # def clena_email(self):
    #     email=self.cleaned_data.get("email")
    #     return email
    # def clean_mensaje(self):
    #     mensaje = self.cleaned_data.get("mensaje")
    #     return mensaje

    nombre = forms.CharField(required=False)
    email =forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)

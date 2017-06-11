#para enviar email
from django.conf import settings
from django.core.mail import send_mail

from django.shortcuts import render
from .forms import RegModelForm, ContactForm
from .models import Registrado
# Create your views here.

def inicio(request):
	titulo = "Bienvenido"
	
	if request.user.is_authenticated():
		titulo ="Bienvenid@ %s" %(request.user)
	form = RegModelForm(request.POST or None)
	# para que no salga a cada rato los textos recordatorios del form

	context = {
		"titulo":titulo,
		"el_form":form,
		}
		
	if form.is_valid():
		instance = form.save(commit=False)
		nombre = form.cleaned_data.get("nombre")
		email = form.cleaned_data.get("email")
		if not instance.nombre:
			instance.nombre = "Persona"
		instance.save()
		context = {
			"titulo": "Gracias %s!" %(nombre)
			}
		if not nombre:
			context = {
				"titulo": "Gracias %s!"%(email)
				}
		# print instance
		# print instance.timestamp
		# form_date = form.cleaned_data #guardar los datos limpios
		# abc = form_date.get("email") #valiable para comparar despues
		# abc2 = form_date.get("nombre")
		# obj = Registrado.objects.create(email=abc, nombre=abc2) #variable abc, es cualqueire
	if request.user.is_authenticated() and request.user.is_staff:
		queryset = Registrado.objects.all().order_by("-timestamp") #.filter(nombre__icontains="" o puede ser iexact)
		context = {
			"queryset": queryset,
		}
	return render(request, "inicio.html", context)

def contact(request):
	titulo= "Contacto"
	form = ContactForm(request.POST or None)
	#hacer en el model tambien el modelo de contacto

	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_mensaje = form.cleaned_data.get("mensaje")
		form_nombre = form.cleaned_data.get("nombre")
		
		asunto = 'Form de Contacto'
		email_from= settings.EMAIL_HOST_USER
		email_to=[email_from,]#gregar despues de la [], "otro email"
		email_mensaje = "%s: %s enviado por %s"%(form_nombre,form_mensaje,form_email)
		send_mail(asunto,
			email_mensaje,
			email_from,
			email_to,
			fail_silently=False)
		#for key, value in form.cleaned_data.iteritems():
			#print key, value
			#form.save()
		# for key in form.cleaned_data:
		# 	print key
		# 	print form.cleaned_data.get(key)

		#print email, mensaje, nombre
	context = {"contacto":form,
			"titulo":titulo,}
	return render(request, "forms.html", context)
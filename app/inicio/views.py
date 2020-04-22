from django.conf import settings
from django.shortcuts import render, redirect

from django.views.generic import (
    TemplateView,
    )

from django.http import HttpResponse
from django.contrib import messages
from django.template.loader import  get_template
from django.core.mail import EmailMultiAlternatives

# Create your views here.
def send_mail(nom, asu, email, men):
    context = {'nom':nom, 'asu':asu, 'email':email, 'men':men}
    template = get_template('inicio/correo.html')
    content = template.render(context)

    asunto = "Web Personal ("+asu+")"
    des = "Enviado desde la Web Personal"
    destino = 'link_2618@hotmail.com'

    correo = EmailMultiAlternatives(asunto, des, settings.EMAIL_HOST_USER, [destino])
    correo.attach_alternative(content, "text/html")
    correo.send()

def Inicio(request):
    template_name = 'inicio/index.html'

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        asunto = request.POST.get('asunto')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        send_mail(nombre, asunto, email, mensaje)

        messages.success(request, 'El mensaje ha sido enviado con exito.')
        return redirect("inicio:inicio")
        #return HttpResponse('El mensaje ha sido enviado con exito.')

    return render(request, template_name, {})

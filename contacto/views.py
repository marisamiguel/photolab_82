from django.http import request
from django.shortcuts import redirect, render
from .forms import FormularioContacto

from django.core.mail import EmailMessage

# Create your views here.La informacin queda almacenada en las variables


def contacto (request):
   formulario_contacto=FormularioContacto()

   if request.method=="POST":
      formulario_contacto=FormularioContacto(data=request.POST)
      if formulario_contacto.is_valid():
         nombre=request.POST.get("nombre")
         apellidos=request.POST.get("apellidos")
         email=request.POST.get("email")
         contenido=request.POST.get("contenido")

         email=EmailMessage("Mensaje desde App Django",
         "El usuario con nombre {} y apellidos {} con la dirección de email {} escribe lo siguiente:\n\n {}".format(nombre,apellidos,email,contenido),
         "",["miguelarnalmarisa@gmail.com"],reply_to=[email])

         try:
            email.send() 
            return redirect("/contacto/?valido")
         except:
            return redirect("/contacto/?novalido")

      
             
   return render(request,"contacto/contacto.html", {'miformulario':formulario_contacto})
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import TemplateView
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage



# Create your views here.
class HomePageView(TemplateView):

    template_name = "index.htm"

    def get(self, request, *args, **kwargs):    
        return render(request, self.template_name,{'Titulo':'Texto de titulo'})
      
def contacto(request):
    formContact = ContactForm()

    # Validar la peticion post
    if request.method == "POST":
        formContact = ContactForm(data=request.POST)    
        if formContact.is_valid():
            nombre = request.POST.get('nombre', '') 
            correo = request.POST.get('correo', '') 
            telefono = request.POST.get('telefono', '')
            mensaje = request.POST.get('mensaje', '')

            # Creamos el objeto con variable del formulario
            # Objeto email
            email = EmailMessage( 

                "Tienes un nuevo mensaje",  # El formato trae los datos del formulario
                "De {} <{}>\n\nEscribio:\n\n{}\n\nTelefono :{}".format(nombre,correo,mensaje,telefono),
                "no-contestar@inbox.mailtrap.io",
                ["jdceballos440@misena.edu.co","juanceballos1911@gmail.com"], # Lista donde se va enviar el correo
                reply_to=[correo],
                
            )
            # Enviar correo
            try:
                email.send()
                return redirect(reverse('contacto')+"?okay")
            except:
            # Envia mensaje
                return redirect(reverse('contacto')+"?fallido")

    return render(request, 'contacto.htm', {'formulario':formContact})
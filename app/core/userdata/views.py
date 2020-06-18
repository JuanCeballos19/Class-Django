from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import reverse



# Create your views here.
class NosotrosPageView(TemplateView):

    template_name = "nosotros.htm"   

    def get(self, request, *args, **kwargs): 
        return render(request, self.template_name,{'titulous':'Nosotros', 'descripcion':'esta es la descripcion'}) 
  
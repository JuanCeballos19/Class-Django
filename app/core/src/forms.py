from django import forms

# Creamos las clases con los formularios:
class ContactForm(forms.Form):
    # Atributos del formulario:
    nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe tu Nombre'}))
    correo = forms.EmailField(label="Email", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe tu Correo'}))
    telefono = forms.CharField(label="Telefono", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe tu Telefono'}))
    mensaje = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe tu Mensaje'}))
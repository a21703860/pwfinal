from django.forms import ModelForm, forms
from .models import Contacto, Comentario


class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
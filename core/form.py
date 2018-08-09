from django.forms import ModelForm
from .models import Ativo, Tipo, Server, Usuario


class FormAtivo(ModelForm):
    class Meta:
        model = Ativo
        fields = '__all__'


class FormTipo(ModelForm):
    class Meta:
        model = Tipo
        fields = '__all__'


class FormServer(ModelForm):
    class Meta:
        model = Server
        fields = '__all__'


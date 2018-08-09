from django.contrib import admin
from .models import Usuario, Tipo, Ativo, Server

# Register your models here.

class AtivoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'modelo', 'fabricante',
                    'descricao', 'mac', 'ip', 'usuario',
                    'senha', 'local', 'atualizacao',
                    'outros')

    def tipo(self, objeto):
        return objeto.tipo


class ServerAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ip', 'usuario',
                    'senha', 'descricao')


admin.site.register(Usuario)
admin.site.register(Tipo)
admin.site.register(Ativo, AtivoAdmin)
admin.site.register(Server, ServerAdmin)

from tastypie.resources import ModelResource
from tastypie import fields, utils
from task.models import *
from django.contrib.auth.models import User
from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized

class UsuarioResource(ModelResource):
    def obj_delete_list(self, bundle, **kwargs):
        # print (bunble.date)
        raise Unauthorized('Ação invalida! Não altorizado para realizar está ação.')


    class Meta:
        queryset = Usuario.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "nome": ('exact', 'startswith',)
        }



class ProjetoResource(ModelResource):
    def obj_delete_list(self, bundle, **kwargs):
        # print (bunble.date)
        raise Unauthorized('Ação invalida! Não altorizado para realizar está ação.')

    class Meta:
        queryset = Projeto.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "nome": ('exact', 'startswith',)
        }



class TarefasResource(ModelResource):
    usuario = fields.ToOneField(UsuarioResource, 'usuario')
    projeto = fields.ToOneField(ProjetoResource, 'projeto')

    def obj_create(self, bundle, **kwargs):
        p = bundle.data['projeto'].split("/")

        tipo = Tarefas()
        tipo.nome = bundle.data['nome'].upper()

        if not (Tarefas.objects.filter(projeto=p[4], nome=tipo)):

            tipo.nome = bundle.data["nome"]
            tipo.dataEHoraDaInscricao = bundle.data["dataEHoraDaInscricao"]
            tipo.usuario = Usuario.objects.get(pk=int(p[4]))
            tipo.projeto = Projeto.objects.get(pk=int(p[4]))

            tipo.save()
            bundle.obj = tipo
            return bundle

        else:
            raise Unauthorized('Tarefa já está cadastrada a um projeto!')

    def obj_delete_list(self, bundle, **kwargs):
        # print (bunble.date)
        raise Unauthorized('Ação invalida! Não altorizado para realizar está ação.')

    class Meta:
        queryset = Tarefas.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "nome": ('exact', 'startswith',)
        }



class PojetoUsuarioResource(ModelResource):
    def obj_delete_list(self, bundle, **kwargs):
        # print (bunble.date)
        raise Unauthorized('Ação invalida! Não altorizado para realizar está ação.')

    class Meta:
        queryset = ProjetoUsuario.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "nome": ('exact', 'startswith',)
        }
from django.conf.urls import url, include
from tastypie.api import Api
from django.contrib import admin
from task.api.resources import *


v1_api = Api(api_name='v1')
v1_api.register(UsuarioResource())
v1_api.register(ProjetoResource())
v1_api.register(TarefasResource())
v1_api.register(PojetoUsuarioResource())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(v1_api.urls)),
]

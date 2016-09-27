"""personal_finance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from finance.models import Movimento, TipoMovimento, Investimento
from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from django.template.context_processors import request
from rest_framework.decorators import api_view
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.parsers import JSONParser

#serializers for models
class MovimentoSerializer(serializers.Serializer):
    try:
        tipo_movimento = serializers.PrimaryKeyRelatedField(queryset=TipoMovimento.objects.all())
        investimento = serializers.PrimaryKeyRelatedField(queryset=Investimento.objects.all())
    except Exception as e:
        print("erro no serializer")
        print(e)
        raise e
    class Meta:
        model = Movimento
        fields = ('investimento', 'tipo_movimento', 'data_movimento', 'valor_movimento')
    
class MovimentoViewSet(viewsets.ModelViewSet):
    queryset = Movimento.objects.all()
    serializer_class = MovimentoSerializer
    
    def create(self, request):
        print("Entrou no ViewSet")
        print(self.action)
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        if serializer.is_valid():

            return Response(
            serializer.validated_data, status=status.HTTP_201_CREATED
            )

@api_view(['GET', 'POST'])
def movimentacao(request, format=None):
    if request.method == 'GET':
        movimentos = Movimento.objects.all()
        serializer = MovimentoSerializer(movimentos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        try:
            print("metodo post")
            print(request)
            #print (request.data)
            #json_data = JSONParser().parse(request.data)
            #print(json_data)
            serializer = MovimentoSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                print("erro no else view")
                print(serializer.errors)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            raise e
        return None

#routers rest
router = routers.DefaultRouter()
router.register(r'movimentos', MovimentoViewSet)

#urls
urlpatterns = [
#    url(r'^', include(router.urls)),
    url(r'^movimentacao/$', movimentacao),
    url(r'^admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)
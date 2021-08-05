from rest_framework import serializers 
from dados.models import Dado
 
 
class DadoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Dado
        fields = ('id',
                  'email',
                  'cpf')
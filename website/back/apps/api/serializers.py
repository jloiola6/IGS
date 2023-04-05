from rest_framework import serializers
 
from back.apps.core.models import Collaborator, Departament
 
 
# Criando modelo de serializer


class DepartamentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departament
        fields = ('id', 'name', 'created_on', 'updated_on')


class CollaboratorSerializer(serializers.HyperlinkedModelSerializer):
    departament = serializers.ReadOnlyField(source='departament.id')   
    departament_id = serializers.PrimaryKeyRelatedField(queryset=Departament.objects.all(), source='departament', write_only=True)
    
    # Especificando campos do modelo
    class Meta:
            model = Collaborator
            fields = ('id', 'name', 'email', 'departament_id', 'departament', 'created_on', 'updated_on')
        
    def create(self, validated_data):
        collaborator = Collaborator.objects.create(**validated_data)
        
        return collaborator
        


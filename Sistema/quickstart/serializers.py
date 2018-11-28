from Sistema.models import Persona, Mascota

from rest_framework import serializers

class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = ('nombrePersona', 'apellidoPersona' )


class MascotaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mascota
        fields = ('nombreMascota', 'estadoMascota' )
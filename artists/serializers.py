from rest_framework import serializers
from .models import Artist

class ArtistSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Artist
		fields = ('first_name', 'second_name')

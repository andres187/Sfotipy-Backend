from django.shortcuts import render

from django.views.generic.detail import DetailView

from .models import Artist

class ArtistDetailView(DetailView):
	model = Artist

	def get_template_names(self):
		return 'artist.html'

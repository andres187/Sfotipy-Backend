import json
#import time
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import ListView

from .models import Track
from django.views.decorators.cache import cache_page
from django.core.cache import cache

#@cache_page(60)

class TrackListView(ListView):
	model = Track
	context_object_name = 'tracks'
	template_name = 'track.html'

@login_required
def track_view(request, title):
	track = get_object_or_404(Track, title=title)
	data = {
		'title': track.title,
		'order': track.order,
		'album': track.album.title,
		'artist': {
			'name': track.artist.first_name,
			'bio': track.artist.biography, 
		}
	}
	#json_data=json.dumps(data)
	#time.sleep(5)
	#return HttpResponse(json_data, content_type='application/json')
	return render(request, 'track.html', {'track': track})



	
from rest_framework import viewsets

class TrackViewSet(viewsets.ModelViewSet):
	model = Track

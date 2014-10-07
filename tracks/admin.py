from django.contrib import admin

from .models import Track

class TrackAdmin(admin.ModelAdmin):
	list_display = ('title', 'order', 'artist', 'album', 'player')
	list_filter = ('artist', 'album')
	search_fields = ('title', 'artist__first_name', 'album__title')
	list_editable = ('artist', 'album')
	raw_id_fields = ('artist',)

admin.site.register(Track, TrackAdmin)


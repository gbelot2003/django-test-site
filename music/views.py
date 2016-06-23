from django.http import HttpResponse

def index(request):
	return HttpResponse("<h2>This is the music App")

def detail(request, album_id):
	return HttpResponse("<h2>Details for Album id: " +  str(album_id) + "</h2>")

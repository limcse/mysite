from django.http import HttpResponse


def index(request):
	return HttpResponse("<h1><center>hello,world!你好，世界！</h1>")
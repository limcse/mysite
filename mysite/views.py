from django.http import HttpResponse


def index(request):
	return HttpResponse("hello,world!你好，世界！")
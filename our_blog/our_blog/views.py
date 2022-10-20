from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hola. Esta es nuesrta primer vista en Django")
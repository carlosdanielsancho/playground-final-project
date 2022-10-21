from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("<h1>Hola.</h1> /n <h2>Esta es nuesrta primer vista en Django!</h2>")
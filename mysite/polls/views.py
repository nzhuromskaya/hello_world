from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    return HttpResponse("Hello, world. This is Sean's message.")
    return HttpResponse("Hello, world. This is Nataliya's message.")
    return HttpResponse("Hello, world. This is Adele's message.")

# Create your views here.

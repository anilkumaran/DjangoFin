from django.http import HttpResponse


def get_laptops(request):
    return HttpResponse("MacBook, HP, DELL, Lenovo")
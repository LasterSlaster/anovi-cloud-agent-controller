import requests
from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Request


def index(request):
    latest_request_list = Request.objects.order_by('request_date')[:100]
    context = {'latest_request_list': latest_request_list}
    return render(request, 'api/index.html', context)

def request(request, request_id):
    try:
        r = Request.objects.get(pk=request_id)
    except Request.DoesNotExist:
        raise Http404("Question does not exist")
    response = requests.post(r)
    print(response.text)
    return render(request, 'api/request.html', {'request': r, 'response': response.text})

def response(request, request_id):
    response = "You're looking at response %s."
    return HttpResponse(response % request_id)


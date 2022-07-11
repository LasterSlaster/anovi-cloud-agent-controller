import json
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
        print(r)
    except Request.DoesNotExist:
        raise Http404("Question does not exist")
    response = requests.post(r)
    print(response.text)
    return render(request, 'api/request.html', {'request': r, 'response': response.text})

def response(request, request_id):
    response = "You're looking at response %s."
    return HttpResponse(response % request_id)

def createDID(request):
    print("Call Aca-Py: create DID and store in wallet")
    create_did_response = requests.post("http://0.0.0.0:8021/wallet/did/create")
    response_json = create_did_response.json()
    print("Create DID result: " + json.dumps(response_json))
    did = response_json['result']['did']
    verkey = response_json['result']['verkey']

    print("Call Aca-Py: publish newly created DID on the ledger")
    register_did_respose = requests.post(f"http://0.0.0.0:8021/ledger/register-nym?did={did}&verkey={verkey}", )
    print("Publish DID result: " + json.dumps(register_did_respose.json()))
    response_data = {}
    response_data['did'] = did
    return HttpResponse(json.dumps(response_data), content_type="application/json")


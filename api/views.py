from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .contractcalls import set_url as set_url_function
from web3 import Web3

@api_view(["POST", "GET"])
def set_url(request):
    try:
        url = str(request.data["url"])
        print(url)
        tx_id = set_url_function(url)
        return Response({"status": "Success","response": tx_id})
    except Exception as e:
        print(e)
        return Response({"status": "Failed"})
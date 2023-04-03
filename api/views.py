from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .contractcalls import set_url as set_url_function, get_url as get_url_function, get_url_by_address, delete_url as delete_url_function
from web3 import Web3

@api_view(["POST", "GET"])
def set_url(request):
    try:
        account = Web3.toChecksumAddress(request.data["account"])
        url = str(request.data["url"])
        print(account)  
        print(url)
        tx_hash = set_url_function(account,url)
        return Response({"status": "Success","response": tx_hash})
    except Exception as e:
        print(e)
        return Response({"status": "Failed"})
    
@api_view(["POST", "GET"])
def get_url(request):
    try:
        account = Web3.toChecksumAddress(request.data["account"])
        print(account)
        url_data = get_url_by_address(account)
        return Response({"status": "Success","response": url_data})
    except Exception as e:
        print(e)
        return Response({"status": "Failed"})
    

@api_view(["POST", "GET"])
def delete_url(request):
    try:
        account = Web3.toChecksumAddress(request.data["account"])
        print(account)
        delete_url_function(account)
        return Response({"status": "Success"})
    except Exception as e:
        print(e)
        return Response({"status": "Failed"})
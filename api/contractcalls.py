from django.shortcuts import render
from django.conf import settings
from rest_framework.response import Response
from web3 import Web3
from web3.middleware import geth_poa_middleware
from . import contract_config
import json
import os


# Contract data
contract_address = contract_config.config["contract_address"]
public_key = contract_config.config["public_key"]
private_key = contract_config.config["private_key"]
contract_filepath = os.path.join(settings.BASE_DIR, "api/contractabi.json")

with open(contract_filepath, "r") as file:
    contract_json = json.load(file)
abi = contract_json["abi"]
bytecode = contract_json["bytecode"]

#blochain connection
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
w3.eth.defaultAccount = public_key
w3.middleware_onion.inject(geth_poa_middleware, layer=0)




def set_url(account,url):
    print("calling contract")
    my_contract = w3.eth.contract(address=contract_address, abi=abi)
    nonce = w3.eth.get_transaction_count(public_key)
    url_tx = my_contract.functions.setURL(account,
        url).build_transaction(
        {
            "from": public_key,
            "nonce": nonce,
            "gasPrice": w3.eth.gas_price,
        }
    )
    signed_transaction = w3.eth.account.sign_transaction(
        url_tx, private_key=private_key
    )
    tx_data = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    receipt = w3.eth.wait_for_transaction_receipt(tx_data)
    url_data = my_contract.functions.getUrlByaddress(account).call()
    return url_data


def get_url(account):
    print("calling contract")
    my_contract = w3.eth.contract(address=contract_address, abi=abi)
    url_tx = my_contract.functions.getURL().call()
    return url_tx

def get_url_by_address(account):
    print("calling contract")
    my_contract = w3.eth.contract(address=contract_address, abi=abi)
    url = my_contract.functions.getUrlByaddress(account).call()
    return url

def delete_url(account):
    print("calling contract")
    my_contract = w3.eth.contract(address=contract_address, abi=abi)
    nonce = w3.eth.get_transaction_count(public_key)
    tx_hash = my_contract.functions.deleteURL(account).build_transaction(
        {
            "from": public_key,
            "nonce": nonce,
            "gasPrice": w3.eth.gas_price,
        }
    )
    signed_transaction = w3.eth.account.sign_transaction(
        tx_hash, private_key=private_key
    )
    tx_data = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    receipt = w3.eth.wait_for_transaction_receipt(tx_data)
    return receipt
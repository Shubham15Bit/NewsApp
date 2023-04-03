from scripts.tools import get_account
from brownie import URLStorage
import json

def deploy_contract():
    account = get_account()
    urlStorage = URLStorage.deploy({"from": account})
    deployed_contract = {"deployed_contract": urlStorage.address}
    with open("deployed_contract.json", "w") as file:
        json.dump(deployed_contract, file)

def main():
    deploy_contract()

from distutils.command.config import config
from scripts.helpful_scripts import get_account
from brownie import interface, network, config

def main():
    get_weth()


def get_weth():
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from":account,"value":0.01*10**18})
    print(f"Received 0.01 WETH")
    return tx
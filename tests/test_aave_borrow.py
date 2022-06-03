from scripts.aave_borrow import(get_asset_price, get_lending_pool, approve_erc20,get_account)
from brownie import config, network


def test_get_assest_price():
    #Arrange/Act
    asset_price = get_asset_price()
    #assert
    assert asset_price > 0

def test_get_lending_pool():
    lending_pool = get_lending_pool()
    assert lending_pool is not None

def test_approve_erc20():
    account = get_account()
    lending_pool = get_lending_pool()
    amount = 1000000000000000000
    erc20_address = config['networks'][network.show_active()]['weth_token']
    tx= approve_erc20(amount,lending_pool.address, erc20_address,account)
    assert tx is not True

from brownie import Dogshit, accounts

def main():
    compte = accounts.load('crazydog')
    t = Dogshit.deploy({'from': compte})

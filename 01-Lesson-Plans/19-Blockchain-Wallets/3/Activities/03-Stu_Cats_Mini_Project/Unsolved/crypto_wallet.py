# Imports
import os
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account, Web3
from web3.gas_strategies.time_based import medium_gas_price_strategy

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))


# Wallet functionality

#@TODO create a function called generate account do not forget to add each of the following steps

def generate_account():
    """Create a digital wallet and Ethereum account from a mnemonic seed phrase."""
    # Access the mnemonic phrase from the `.env` file
    mnemonic = os.getenv("MNEMONIC")

    # Create Wallet object instance
    wallet = Wallet(mnemonic)

    # Derive Ethereum private key
    private, public = wallet.derive_account("eth")

    # Convert private key into an Ethereum account
    account = Account.privateKeyToAccount(private)

    # Return the account from the function
    return account
    
#@TODO create a function called generate account do not forget to add each of the following steps
def get_balance(address):
    """Using an Ethereum account address access the balance of Ether"""
    #Call the w3.eth.get_balance function and pass it the address argument. Set this function call equal to a variable called wei_balance
    wei_balance = w3.eth.get_balance(address)

    #Call the w3.fromWei function and pass it wei_balance as an argument. Specify that you want to convert the wei balance to ether. Set this call equal to a variable called ether.
    ether = w3.fromWei(wei_balance, 'ether')

    #Return the `ether` balance from the function.
    return ether


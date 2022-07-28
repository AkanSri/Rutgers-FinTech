# Ethereum Account Functions

################################################################################

# Imports
import os
import requests
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
################################################################################

# Create a function called `generate_account` that automates the Ethereum
# account creation process
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


# @TODO
# Create a function called `get_balance`, it should convert the wei balance of the account to ether, and returns the value of ether
def get_balance(address):
    #Call the w3.eth.get_balance function and pass it the address argument. Set this function call equal to a variable called wei_balance
    wei_balance = w3.eth.get_balance(address)

    #Call the w3.fromWei function and pass it wei_balance as an argument. Specify that you want to convert the wei balance to ether. Set this call equal to a variable called ether.
    ether = w3.fromWei(wei_balance, 'ether')

    #Return the `ether` balance from the function.
    return ether

# @TODO
# Create a function called `send_transaction` that creates a raw transaction, signs it, and sends it. Return the confirmation hash from the transaction.
def send_transaction(account, receiver,  ether):
    #Set a medium gas price strategy
    w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

    #Call the w3.teWei function and pass it the argument ether. You will also need to specify that "ether" is the denomination of the value being converted. Finally, set this function call equal to the variable wei_value.
    wei_value = w3.toWei(ether, "ether")
    
    #Estimate the gas it will take to mine the transaction. Call the function w3.eth.estimateGas and pass it three arguments as key:value pairs
    gas_estimate = w3.eth.estimateGas({"to": receiver, "from": account.address, "value" : wei_value})
    gas_price = 0

    #Construct the transaction object. Set the transaction object equal to the variable raw_tx. The keys you will need complete are: "to", "from", "value", "gas", "gasPrice" (the corresponding value is w3.eth.generateGasPrice) and the "nonce" (the corresponding value is `w3.eth.getTransactionCount(account.address)).
    raw_tx = {"to": receiver, "from": account.address, "value" : wei_value, "gas":gas_estimate, "gasPrice":gas_price, "nonce":w3.eth.getTransactionCount(account.address)}

    #Call the account.signTransaction function and pass it the raw_tx as an argument. Set this equal to a variable called signed_tx
    signed_tx = account.signTransaction(raw_tx)

    #Return the w3.eth.sendRawTransaction function. You will need to pass signed_tx.rawTransaction as the function argument.
    return w3.eth.sendRawTransaction(signed_tx.rawTransaction)

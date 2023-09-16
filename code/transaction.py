from web3 import Web3
from eth_account import Account

def connect_provider():
    return Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

def get_transaction(w3, contract, account_address, function_name, args):
    nonce = w3.eth.get_transaction_count(account_address)
    data = contract.encodeABI(fn_name=function_name, args=args)
    return {
        'to': contract.address,  
        'value': 0,
        'gas': 2000000,
        'gasPrice': w3.to_wei('50', 'gwei'),
        'nonce': nonce,
        'data': data,  
        'chainId': 1337
    }

def get_account(private_key):
    return Account.from_key(private_key)

def get_contract(w3, contract_address, contract_abi):
    return w3.eth.contract(address=contract_address, abi=contract_abi)

def send_transaction(w3, private_key, transaction):
    signed_tx = w3.eth.account.sign_transaction(transaction, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return w3.eth.wait_for_transaction_receipt(tx_hash)

def main():
    private_key = ''
    contract_address = ''
    contract_abi = [...]
    w3 = connect_provider()
    account = get_account(private_key)
    contract = get_contract(w3, contract_address, contract_abi)

    transaction = get_transaction(w3, contract, account.address, 'store', [444])
    tx_receipt = send_transaction(w3, private_key, transaction)

    print(tx_receipt)

if __name__ == "__main__":
    main()  

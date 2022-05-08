import requests as rq
import pandas as pd

def link_address_history(address, chain_id):
    api_key = 'ckey_4e20bd1de6b3424c81eefbd7157'
    url = "https://api.covalenthq.com/v1/{}/address/{}/portfolio_v2/?key={}".format(chain_id, address, api_key)
    r = rq.get(url).json()['data']['items'][0]['holdings']
    df = pd.DataFrame(r)

    return(df)


if __name__ == '__main__':
    print(link_address_history("0xb71f6064b01c7e2e14f3bb93db665400ac7acb37", 1))
    
    
'''
Fonction qui prend en argument une adresse et le numero de la blockchain.
Et qui retourne une DataFrame comprenant les élément neccesaire pour annalyser l'historique du wallet
'''
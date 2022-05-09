import pandas as pd
import numpy as np
import os
import warnings
warnings.filterwarnings("ignore")
from src.app.feature_wallet.all_address_wallet import all_address_wallet
from src.app.feature_wallet.wallet import wallet as wallet_function

def group(wallet, chain_id, action, name_folder):
    
    if action == 'add':
        if os.path.exists('./src/app/feature_group/Folder.json') == True:
            df = pd.DataFrame(pd.read_json('./src/app/feature_group/Folder.json'))
            if df[df['name']== name_folder].empty:
                return("Folder doesn't exist")
            else:
                wallets = np.array([wallet, chain_id])
                old = (df[df['name']==name_folder]['wallets']).values
                x = np.append(old[0], wallets)
                df.drop(df[df['name']==name_folder]['wallets'].index, 0, inplace=True)
                temp = []
                new = []
                for i in range(0,len(x),2):
                    temp.append(x[i])
                    temp.append(int(x[i+1]))
                    new.append(temp)
                    temp = []
                cf,total = all_address_wallet(np.array(new))
                folder = {"name" : name_folder,
                            "wallets" : np.array(new),
                            "total_folder" : total}
                list_folder = []
                list_folder.append(folder)
                df = df.append(list_folder, ignore_index=True)
                pd.DataFrame(df).to_json('./src/app/feature_group/Folder.json')
                return(pd.read_json('./src/app/feature_group/Folder.json'))
        else:
            return('erreur dossier inexistant')
        
        
    elif action == 'create':
        if os.path.exists('./src/app/feature_group/Folder.json') == True:
            df = pd.DataFrame(pd.read_json('./src/app/feature_group/Folder.json'))
            if df[df['name']== name_folder].empty:
                wallets = np.array([wallet, chain_id], dtype=object)
                cf,total = wallet_function(wallets[0], wallets[1])
                folder = { "name" : name_folder,
                            "wallets" : wallets,
                            "total_folder" : total}
                list_folder = []
                list_folder.append(folder)
                df = df.append(list_folder, ignore_index=True)
                pd.DataFrame(df).to_json('./src/app/feature_group/Folder.json')
                return(pd.read_json('./src/app/feature_group/Folder.json'))
            else:
                return('erreur dossier existant')
        else:
            wallets = np.array([wallet, chain_id], dtype=object)
            cf,total = wallet_function(wallets[0], wallets[1])
            folder = { "name" : name_folder,
                        "wallets" : wallets,
                        "total_folder" : total}
            list_folder = []
            list_folder.append(folder)
            pd.DataFrame(list_folder).to_json('./src/app/feature_group/Folder.json')
            return(pd.read_json('./src/app/feature_group/Folder.json'))


    elif action == 'delete_folder':
        df = pd.DataFrame(pd.read_json('./src/app/feature_group/Folder.json'))
        df.drop(df[df['name']==name_folder].index, 0, inplace=True)
        pd.DataFrame(df).to_json('./src/app/feature_group/Folder.json')
        return(pd.read_json('./src/app/feature_group/Folder.json'))
    
    
    elif action == 'delete_wallet':
        df = pd.DataFrame(pd.read_json('./src/app/feature_group/Folder.json'))
        old = (df[df['name']==name_folder]['wallets']).values
        temp = []
        for i in range(len(old[0])):
            if old[0][i][0] != wallet:
                temp.append(old[0][i])
        cf,total = all_address_wallet(np.array(temp))   
        folder = {"name" : name_folder,
                    "wallets" : temp,
                    "total_folder" : total}
        list_folder = []
        list_folder.append(folder)
        df.drop(df[df['name']==name_folder]['wallets'].index, 0, inplace=True)
        df = df.append(list_folder, ignore_index=True)
        pd.DataFrame(df).to_json('./src/app/feature_group/Folder.json')
        return(pd.read_json('./src/app/feature_group/Folder.json'))



if __name__ == '__main__':
    # print(group("0xd5Ac26b0FE1D3Ae9A7679cD92598fF02d79A9E26", 1, 'create', 'test1'))
    # print(group("0xd5Ac26b0FE1D3Ae9A7679cD92598fF02d79A9E26", 1, 'add', 'test1'))
    print(group("0xd5Ac26b0FE1D3Ae9A7679cD92598fF02d79A9E26", 1, 'delete_wallet', 'test1'))
    # print(group("12345678909876543212345678", 45345678, 'delete_folder', 'test56'))
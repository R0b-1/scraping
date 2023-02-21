import pandas as pd
import numpy as np
import re


data = pd.read_csv('operations.csv')
# print(data)
def tests():
    data_null = data.isnull().sum()
    print(data.dtypes)
    print(data.isnull().sum())
    print(data_null[data_null>0])



tests()





def datetime():
    data['date_operation'] = pd.to_datetime(data['date_operation'])
    print(data.dtypes)

def montantsNull():
    data.loc[data['montant'].isnull(),:]
    data_null = data.loc[data['montant'].isnull(),:]
    for index in data_null.index:
        data.loc[index, 'montant'] = data.loc[index+1, 'solde_avt_ope'] - data.loc[index,'solde_avt_ope']

montantsNull()


def categNull():
    data.loc[data['categ'].isnull(), 'categ'] = 'FACTURE TELEPHONE'
categNull()
print(data.loc[data['categ'].isnull(),:])
print(data.loc[data['libelle'] == 'PRELEVEMENT XX TELEPHONE XX XX', :])

def duplicate():
    data.drop_duplicates(subset=['date_operation', "libelle", 'montant', 'solde_avt_ope'])



print(data.describe())

def outliers():
    b = data.loc[data['montant']==-15000,:].index[0]
    print(b)
    print(data.iloc[b-1:b+2,:])
#outliers()
data.loc[data['montant']==-15000, 'montant'] = -14.39
print(data.loc[data['montant']==-15000, 'montant'])


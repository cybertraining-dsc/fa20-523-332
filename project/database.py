# -*- coding: utf-8 -*-

!pip install dnspython

import pymongo
import numpy as np
import pandas as pd

def add_batch_data(data_type, index_name):
  client = pymongo.MongoClient("mongodb+srv://kmhatre:" + PASSWORD + "@crypto.j5hw0.mongodb.net/" + data_type + "?retryWrites=true&w=majority")
  db = client[data_type]
  colec = db[index_name]
  if data_type == 'crypto':
    df = pd.read_csv('/content/drive/My Drive/Academics/Fall 2020/Big Data/Final Project/Data/crypto/' + index_name + '_price.csv')
  elif data_type == 'forex':
    df = pd.read_csv('/content/drive/My Drive/Academics/Fall 2020/Big Data/Final Project/Data/Foreign_Exchange_Rates.csv')
    cols = ['Index']
    for i in df.columns[1:]:
      cols.append(i)
    df.columns = cols
  to_add = []
  for i in range(len(df)):
    tmp = {}
    for j in range(len(df.columns)):
      tmp[str(df.columns[j])] = str(df.iloc[i][j])
    to_add.append(tmp)
  colec.insert_many(to_add)
  client.close()

def add_crypto_batch():
  crypto_list = ['bitcoin', 'bitcoin_cash', 'bitconnect', 'dash', 'ethereum', 'ethereum_classic', 'iota', 'litecoin', 
               'monero', 'nem', 'neo', 'numeraire', 'omisego', 'qtum', 'ripple', 'stratis', 'waves']
  for crypto_name in crypto_list:
    add_batch_data('crypto', crypto_name)

def query(data_type, index, key="", value=""):
  client = pymongo.MongoClient("mongodb+srv://kmhatre:" + PASSWORD + "@crypto.j5hw0.mongodb.net/" + data_type + "?retryWrites=true&w=majority")
  db = client[data_type]
  colec = db[index]
  result = colec.find_one({key : value})
  client.close()
  return result
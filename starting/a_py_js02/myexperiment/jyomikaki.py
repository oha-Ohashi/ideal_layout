import time
#---------時書き換えのため
import json 
from collections import OrderedDict
import pprint
#-----------------------


def kaki_json(path, key, value):
    for i in range(3):
        try:
            fname = path
            with open(fname) as f:
                df = json.load(f, object_pairs_hook=OrderedDict)
            df[key] = value
            with open(fname, 'w') as f:
                json.dump(df, f, indent=4)    
        except:
            print('おまたせしてまし  ', end='')
            print(time.time())
            time.sleep(0.5)
            continue


def dict_json(path):
    for i in range(3):
        try:
            fname = path
            with open(fname) as f:
                df = json.load(f, object_pairs_hook=OrderedDict)
            return df 
        except: 
            print('おまたせしてまし  ', end='')
            print(time.time())
            time.sleep(0.5)
            continue
'''
def kaki_json(path, key, value):
    fname = path
    with open(fname) as f:
        df = json.load(f, object_pairs_hook=OrderedDict)
    df[key] = value
    with open(fname, 'w') as f:
        json.dump(df, f, indent=4)    

def dict_json(path):
    fname = path
    with open(fname) as f:
        df = json.load(f, object_pairs_hook=OrderedDict)
    return df 
'''


def add_apo(a):
    fname = 'scripts/oha.json'
    with open(fname) as f:
        df = json.load(f, object_pairs_hook=OrderedDict)
        arr = df['schedule']
    if(a > float(time.time()) and a < float(time.time())+10000000):
        if(a in arr):
            print('重複です')
        else:
            print('追加しました')
            arr.append(a)#追加して
            for ar in arr:
                print(ar)#ダンプ
            df['schedule'] = arr
            with open(fname, 'w') as f:
                json.dump(df, f, indent=4)
    else:
        print('ふてきせつなすうじ')
    
   

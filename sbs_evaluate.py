import random 
import sbs_io as io
import sbs_calc 

def disp_eval(keys):          #紹介します
    print('--------------------')
    print(keys3x10(keys))
    calc = evaluate(keys)
    print("alternate:", calc.n_alternate)
    print("costs:", calc.costs)
    print('cost:', "{:,}".format(calc.cost_sum))
def keys3x10(keys):            #三行にかえる
    l = list(keys)
    index = [(5, ' '),(16, ' '),(27, ' '),(11, '\n'),(23, '\n')]
    for x in index:
        l.insert(x[0], x[1])
    return ''.join(map(str, l))

def evaluate(keys):
    text = 'it is a fine day'
    with open('./txt_to_type/en.txt') as f:
        text += f.read()
    with open('./txt_to_type/ja.txt') as f:
        text += f.read()
    #text = "rand no men known to us could have built this place, nor the men known to our brothers who lived before us, andyet it was built by men.we knelt, and we crawled forward, our hand groping alongthe iron line to see where it would lead.our heart beat in our fingertips"
    #text += 'kanzi ・ kana ma ziri no bunsyou wo 、 hiragana oyo bi ro-ma zi ni sorezore henkan si masu 。ka no tekisuto eria ni nihongo no bunsyou wo nyuuryoku 、 mataha ha rituke te 、 「 henkan zikkou 」 botan wo o si te kuda sai 。saidai 、 8000 mozi made henkan kanou desu 。'
    #text = 'ab'
    sxy = io.StringXY(text, keys)
    xy_array = sxy.string_to_xyarray()
    calc = sbs_calc.Calculation(xy_array)
    return calc


if __name__ == '__main__':
    disp_eval('ABCDEFGHIJKLMNOPQRSTUVWXYZ____')
    disp_eval('QWERTYUIOPASDFGHJKL_ZXCVBNM___')
    disp_eval("___PYFGCRLAOEUIDHTNS_QJKXBMWVZ")
    disp_eval("QWFPBJLUY_ARSTGMNEIOZXCDVKH___")
    disp_eval("QW___MRDYPAOEIUGTKSNZXCVFBHJL_")
    disp_eval("_WBF_MRDYPAOEUIGTKNSZXCV__HJLQ")
    #disp_eval("XPFU__DMWBOEAICSNKTRQVYG__HJLZ")
    #disp_eval("FGSM__CUPXNRKTDYEAOIZHJL__BWVQ")
    disp_eval("GFDM__CYBXRTKNSIAEOUZHJL__PWVQ")
    print("左HJKL固定")
    disp_eval("ZGMK__CWPQDNHTRIEAOUVFLS__YBXJ")
    print("無固定(右母音)")
    disp_eval("QBYC__MDLFIEAOURNTHSJXWP__KGZV")
    print("無固定(左母音)")

   
import sbs_io as io
import sbs_evaluate as ev
import random
random.seed(1)

ms = io.MojiretsuSousa('config.txt')

def search(abc):
    #abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #abc = 'ABCDEFGIMNOPQRSTUVWXYZ'
    n_roop = 2000
    e_max = evaluate(abc)
    for i in range(n_roop):
        new_abc = swap(abc)
        e = evaluate(new_abc)
        if e < e_max:
            #print('{}: {}'.format(i,e))
            abc = new_abc
            e_max = e
    return abc

def swap(string1):
    list1 = list(string1)        
    i = random.randrange(-1, len(list1))
    j = random.randrange(-1, len(list1))
    list1[i], list1[j] = list1[j], list1[i]
    return ''.join(map(str, list1))

def evaluate(s):
    return ev.evaluate(ms.mizuni_modosu(s)).cost_sum


if __name__ == '__main__':
    for i in range(10):
        indv = search(ms.nai_str)
        keys_to_show = io.dead_keys(ms.mizuni_modosu(indv))
        print(keys_to_show)
        print(ev.keys3x10(keys_to_show))
        print(evaluate(indv))
        print()

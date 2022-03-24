import sbs_io as io
import sbs_evaluate as ev
import copy
import random
random.seed(1)

def search2(ms):
    n_roop = 2000
    abc_list = ms.nai_list
    e_max = ev.evaluate(
        ms.mizuni_modosu(abc_list)
    ).cost_sum
    for i in range(n_roop):
        new_abc = swap(abc_list)
        e = ev.evaluate(
            ms.mizuni_modosu(new_abc)
        ).cost_sum
        if e < e_max:
            #print("update!", i)
            abc_list = new_abc
            e_max = e
    return ''.join(map(str, abc_list))

def swap(arg_l):
    list1 = copy.deepcopy(arg_l)
    i = random.randrange(0, len(list1))
    j = random.randrange(0, len(list1))
    list1[i], list1[j] = list1[j], list1[i]
    return list1

if __name__ == '__main__':
    ms = io.MojiretsuSousa('config.txt')
    for i in range(10):
        indv = search2(ms)
        keys_to_show = ms.mizuni_modosu(list(indv))
        print(keys_to_show)
        print(ev.keys3x10(keys_to_show))
        print(ev.evaluate(keys_to_show).cost_sum)
    '''
    for i in range(10):
        indv = search(ms.nai_str)
        keys_to_show = io.dead_keys(ms.mizuni_modosu(indv))
        print(keys_to_show)
        print(ev.keys3x10(keys_to_show))
        print(evaluate(indv))
        print()
    '''

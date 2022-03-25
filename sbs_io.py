import copy
class StringXY:
    def __init__(self, text, keys):
        self.text = text
        self.keys_in1row = keys

    def c_to_xy(self, c):
        c = c.upper()
        index = self.keys_in1row.find(c)
        if index > -1:
            return [index % 10, index // 10]
        else:
            return None
    def string_to_xyarray(self):
        res = []
        for c in self.text:
            if self.c_to_xy(c) != None:
                res.append(self.c_to_xy(c))
        return res


class MojiretsuSousa:
    def __init__(self, path):
        #print(path)
        f = open(path, 'r')
        data = f.read()
        f.close()
        data = list(data)
        data.remove('\n')
        data.remove('\n')
        self.layout_list = data
        self.nai_list = self.aru_nai()
    
    def aru_nai(self):
        nai_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        for c in self.layout_list:
            if c != 'x' and c != '_':
                nai_list.remove(c)
        return nai_list
    
    def mizuni_modosu(self, target):
        target = copy.deepcopy(target)
        modoshi = []
        for i in range(30):
            c = self.layout_list[i]
            if c != 'x':
                modoshi.append(c)
            else:
                item = target.pop(0)
                modoshi.append(item)
        
        modoshi = ''.join(map(str, modoshi))
        return modoshi

if __name__ == '__main__':
    ms = MojiretsuSousa("config.txt")
    #print(ms.layout_list)
    print('nai:', ms.nai_str)
    print('modoshi:', ms.mizni_modosu('FGSDA'))
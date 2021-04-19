import math
import time, datetime
import jyomikaki

print("hello")
jyomikaki.kaki_json("abc.json", 'name', "macchann")
print(jyomikaki.dict_json("abc.json")['name'])
print("world")

''' 何十何.何何秒 (UNIX time) '''
def ssss():
    return math.floor(time.time() % 100 * 100) /100

while True:
    print(ssss())
    jyomikaki.kaki_json("abc.json", 'ssss', ssss())
    time.sleep(1)

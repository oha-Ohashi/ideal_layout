import math

class Calculation:
    def __init__(self, xy_array):
        self.costs = {
            "position": 0,
            "move": 0
        }
        self.xy_array = xy_array
        self.n_alternate = 0
        self.create_cost2()              ##計算し～よお～
        self.costs["move"] = int(self.costs["move"] *100)/100
        self.cost_sum = self.costs["position"] + self.costs["move"]
    
    def create_cost2(self):
        for i, xy in enumerate(self.xy_array):
            #非ホムポジ罰則
            self.costs["position"] += 10*self.position_penalty(self.xy_array[i]) 
            #左右交互打鍵でないときだけ距離はかる
            if i > 0:
                if self.at_left_hand(self.xy_array[i]) \
                == self.at_left_hand(self.xy_array[i-1]): 
                    distance = self.distance_2Darray(
                        self.xy_array[i],
                        self.xy_array[i-1]
                    )
                    #print(distance)
                    # 横移動は多いほうがいい、縦移動は少ないほうがいい
                    self.costs["move"] += (5 - distance["x"]) *3
                    self.costs["move"] += distance["y"]       *3 
                else:
                    self.n_alternate += 1


    positon_cost = [
        [1.5, 1.3, 1.0, 1.0, 1.5,   1.5, 1.0, 1.0, 1.3, 1.5],
        [0.5, 0.3, 0.1, 0.0, 1.0,   1.0, 0.0, 0.1, 0.3, 0.5],
        [2.0, 1.8, 1.2, 1.0, 1.5,   1.5, 1.0, 1.2, 1.8, 2.0],
    ]

    def position_penalty(self, xy):
        return self.positon_cost[xy[1]] [xy[0]]
    def distance_2Darray(self, a, b):
        res = {
            "x": (a[0]-b[0]),
            "y": (a[1]-b[1])
        }
        return res
    def at_left_hand(self, xy):
        #print(xy)
        if xy[0] <= 4:
            #print("left")
            return True
        else:
            #print("right")
            return False



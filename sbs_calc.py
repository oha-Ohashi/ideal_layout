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
                    move_cost = 0
                    distance = self.distance_2Darray(
                        self.xy_array[i],
                        self.xy_array[i-1]
                    )
                    move_cost += distance["x"] *6
                    move_cost += distance["y"] *6 
                    #同じ指を使ったら移動コスト2倍
                    if self.which_fing(self.xy_array[i]) \
                        == self.which_fing(self.xy_array[i-1]):
                        move_cost *= 2

                    self.costs["move"] += move_cost 

                else:
                    self.n_alternate += 1


    positon_cost = [
        [1.5, 1.3, 1.0, 1.0, 1.5,   1.5, 1.0, 1.0, 1.3, 1.5],
        [0.5, 0.3, 0.1, 0.0, 0.5,   0.5, 0.0, 0.1, 0.3, 0.5],
        [2.0, 1.8, 1.2, 1.0, 1.5,   1.5, 1.0, 1.2, 1.8, 2.0],
    ]
    def position_penalty(self, xy):
        return self.positon_cost[xy[1]] [xy[0]]
    def at_left_hand(self, xy):
        #print(xy)
        if xy[0] <= 4:
            #print("left")
            return True
        else:
            #print("right")
            return False
    def distance_2Darray(self, a, b):
        res = {
            "x": abs(a[0]-b[0]),
            "y": abs(a[1]-b[1])
        }
        return res
    finger_list = [
        [1,2,3,4,4, 5,5,6,7,8],
        [1,2,3,4,4, 5,5,6,7,8],
        [1,2,3,4,4, 5,5,6,7,8]
    ]
    def which_fing(self, xy):
        return self.finger_list[xy[1]] [xy[0]]



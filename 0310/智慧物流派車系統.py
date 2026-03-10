#這是一個智慧物流派車系統的實作，包含基底類別 Member 和兩個子類別 VIPMember 與 GoldMember，以及一個 solve_discount 函式來計算最終價格。程式會讀取輸入指令來判斷會員等級和消費金額，並根據會員等級套用相應的折扣率。
import sys
#sys 模組用於讀取標準輸入，方便處理多行輸入指令。
# 1. 基底類別
class Transport:
    def __init__(self, capacity):
        self.capacity = capacity
    def calculate_cost(self, distance):
        return 0

# 2. 卡車類別 [cite: 373]
class Truck(Transport):
    def calculate_cost(self, distance):
        return distance * 20

# 3. 無人機類別 [cite: 374]
class Drone(Transport):
    def calculate_cost(self, distance):
        return distance * 5 + 50

def solve_fleet():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    # 讀取公司工具 [cite: 376]
    n = int(input_data[0])
    fleet = []
    curr = 1
    for _ in range(n):
        t_type = input_data[curr]
        cap = int(input_data[curr+1])
        if t_type == "Truck":
            fleet.append(Truck(cap))
        elif t_type == "Drone":
            fleet.append(Drone(cap))
        curr += 2
        
    # 讀取訂單 [cite: 376]
    m_orders = int(input_data[curr])
    curr += 1
    
    for _ in range(m_orders):
        weight = int(input_data[curr])
        dist = int(input_data[curr+1])
        curr += 2
        
        valid_costs = []
        for t in fleet:
            if t.capacity >= weight: # 過濾載重不足 
                valid_costs.append(t.calculate_cost(dist))
        
        # 找出最低運費 
        if not valid_costs:
            print("No transport available")
        else:
            print(f"Lowest Cost: {min(valid_costs)}")

if __name__ == "__main__":
    solve_fleet()
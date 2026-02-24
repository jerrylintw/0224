import math
people, amount = input().split()
people = int(people)        # 轉換為整數
amount = float(amount)      # 轉換為浮點數

def sharePayment(people, amount):
    # 計算含服務費的總額 (無條件捨去小數)
    total = math.floor(amount * 1.1)
    # 計算個人應付金額 (無條件捨去小數)
    per_person = math.floor(total / people)
    
    print(f"Total: NT${total}, Per person: NT${per_person}")

sharePayment(people, amount)  # 呼叫函數
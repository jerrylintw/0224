# 這是一個銀行自訂例外外防護的實作，程式會定義兩個自訂例外類別 NegativeAmountError 和 InsufficientFundsError，並在 BankAccount 類別中使用這些例外來處理存款和提款的錯誤情況。程式會讀取多行輸入，第一行包含交易筆數 N，接下來 N 行包含交易指令和金額，最後輸出最終餘額。
import sys
#sys 模組用於讀取標準輸入，方便處理多行輸入指令。
# 1. 自訂例外類別 (繼承自 Exception)
class NegativeAmountError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

# 2. 銀行帳戶類別
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            raise NegativeAmountError() # 負數金額拋出例外
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise NegativeAmountError() # 負數金額拋出例外
        if amount > self.balance:
            raise InsufficientFundsError() # 餘額不足拋出例外
        self.balance -= amount

def solve_bank_system():
    # 讀取所有輸入資料
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0]) # 交易筆數
    account = BankAccount()
    curr = 1
    
    for _ in range(n):
        if curr >= len(input_data): break
        
        cmd = input_data[curr]
        amount = int(input_data[curr + 1])
        
        try:
            if cmd == "D":
                account.deposit(amount)
            elif cmd == "W":
                account.withdraw(amount)
            print("Success") # 成功輸出
        except NegativeAmountError:
            # 修正處：移除結尾句點
            print("Error: Amount cannot be negative") 
        except InsufficientFundsError:
            print("Error: Insufficient funds")
            
        curr += 2
        
    # 最後輸出最終餘額
    print(f"Final Balance: {account.balance}")

if __name__ == "__main__":
    solve_bank_system()
# 這是一個安全除法計算器的實作，程式會讀取多行輸入，每行包含兩個數字，並嘗試進行整數除法。程式會處理無效輸入和除以零的情況，並輸出相應的錯誤訊息。
import sys
#sys 模組用於讀取標準輸入，方便處理多行輸入指令。
def safe_division_calculator():
    # 使用 sys.stdin 讀取所有輸入內容，避免 EOF 報錯
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # 第一行是查詢筆數 N
    n = int(input_data[0])
    curr = 1
    
    for _ in range(n):
        if curr + 1 >= len(input_data):
            break
            
        x_str = input_data[curr]
        y_str = input_data[curr + 1]
        
        try:
            # 嘗試轉成整數並執行整數除法
            x = int(x_str)
            y = int(y_str)
            result = x // y
            print(result)
        except ValueError:
            # 捕捉無效的數字格式 (例如 A)
            print("Error: Invalid input")
        except ZeroDivisionError:
            # 捕捉除以零錯誤
            print("Error: Division by zero")
            
        curr += 2

if __name__ == "__main__":
    safe_division_calculator()
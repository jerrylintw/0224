import sys

# 自訂例外類別 
class InvalidDataError(Exception):
    pass

def solve_parser():
    input_data = sys.stdin.read().splitlines()
    if not input_data: return
    
    n = int(input_data[0])
    
    for i in range(1, n + 1):
        row_str = input_data[i]
        try:
            # 1. 檢查欄位數量 
            fields = row_str.split(',')
            if len(fields) != 3:
                raise ValueError("Missing fields")
            
            name = fields[0].strip()
            # 2. 檢查型態轉換 
            age = int(fields[1].strip())
            height = float(fields[2].strip())
            
            # 3. 檢查邏輯錯誤 
            if age < 0 or height <= 0.0:
                raise InvalidDataError()
            
            print(f"Row {i}: Success") # [cite: 463]
            
        except ValueError:
            # 欄位缺少或型態錯誤統一捕捉 [cite: 464]
            print(f"Row {i}: Format Error")
        except InvalidDataError:
            # 邏輯錯誤捕捉 [cite: 465]
            print(f"Row {i}: Logical Error")

if __name__ == "__main__":
    solve_parser()
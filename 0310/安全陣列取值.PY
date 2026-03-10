# 這是一個安全陣列取值的實作，程式會讀取多行輸入，第一行包含一個商品清單，第二行包含查詢筆數 M，接下來 M 行包含要查詢的索引。程式會嘗試將索引轉換為整數並從商品清單中取值，並處理非數字輸入和索引超出範圍的情況，輸出相應的錯誤訊息。
import sys
#sys 模組用於讀取標準輸入，方便處理多行輸入指令。
def safe_array_access():
    # 使用 splitlines 讀取，避免格式混亂
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
        
    # 第一行：商品清單
    items = input_data[0].split()
    # 第二行：查詢筆數 M
    if len(input_data) < 2: return
    m = int(input_data[1])
    
    # 接下來 M 行查詢
    for i in range(2, 2 + m):
        if i >= len(input_data): break
        index_str = input_data[i].strip()
        
        try:
            # 1. 嘗試轉換為整數 (可能發生 ValueError)
            idx = int(index_str)
            
            # 2. 嘗試取值 (可能發生 IndexError)
            print(items[idx])
            
        except ValueError:
            # 處理非數字輸入 (如 "Two")
            print("Error: Invalid index type")
        except IndexError:
            # 處理超出範圍 (如清單 3 個，查索引 5)
            print("Error: Index out of bounds")

if __name__ == "__main__":
    safe_array_access()
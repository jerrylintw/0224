# 這個程式用來計算庫存商品的總價值，通過價格乘以數量。
import sys  # 引入sys模組，用來讀取標準輸入
import pandas as pd  # 引入pandas庫，用來處理表格數據

class Inventory:  # 定義庫存類別
    def __init__(self, data):  # 初始化，接收數據
        # 將傳入的字典列表轉換為 Pandas DataFrame，就像把數據放進表格
        self.df = pd.DataFrame(data, columns=['Item', 'Price', 'Quantity'])

    def calculate_total_value(self):  # 方法來計算總價值
        # 使用 Pandas 向量化運算：Price * Quantity 得到 Total_Value，就像每行乘法
        self.df['Total_Value'] = self.df['Price'] * self.df['Quantity']
        return self.df  # 回傳數據框

def solve_inventory():  # 主函數
    input_data = sys.stdin.read().split()  # 讀取輸入
    if not input_data: return  # 如果沒有，結束

    n = int(input_data[0])  # 商品數量
    items = []  # 列表存商品
    idx = 1  # 索引

    # 解析輸入資料
    for _ in range(n):  # 循環商品數
        name = input_data[idx]  # 名稱
        price = int(input_data[idx+1])  # 價格
        qty = int(input_data[idx+2])  # 數量
        # 將每筆資料存成字典
        items.append({'Item': name, 'Price': price, 'Quantity': qty})
        idx += 3  # 前進

    # 建立 Inventory 物件並計算
    inv = Inventory(items)  # 創建庫存
    result_df = inv.calculate_total_value()  # 計算

    # 輸出 ItemName 與 Total_Value
    for index, row in result_df.iterrows():  # 遍歷
        print(f"{row['Item']} {row['Total_Value']}")  # 印出

if __name__ == "__main__":  # 如果直接運行
    solve_inventory()  # 呼叫
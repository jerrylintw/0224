# 這個程式用來處理電商資料，填補缺失價格，按分類計算總金額並按字母順序排序輸出。
import sys  # 引入sys模組，用來讀取標準輸入
import pandas as pd  # 引入pandas庫，用來處理表格數據
import numpy as np  # 引入numpy庫，用來處理數值

class DataPipeline:  # 定義資料管線類別
    def __init__(self, data):  # 初始化，接收數據
        # 建立 DataFrame，就像把數據放進表格
        self.df = pd.DataFrame(data, columns=['Category', 'Item', 'Price'])
        # 強制將 Price 轉為數字，無效字串 (如 'NaN') 會變成真正的 np.nan，就像把字串變成數字
        self.df['Price'] = pd.to_numeric(self.df['Price'], errors='coerce')

    def process_data(self):  # 方法來處理數據
        # 1. 針對各個 Category，用該分類的平均值填補缺失值，就像用同類的平均填空
        self.df['Price'] = self.df.groupby('Category')['Price'].transform(
            lambda x: x.fillna(x.mean())
        )

        # 2. 分組加總總金額，就像把同分類的價格加起來
        report = self.df.groupby('Category', as_index=False)['Price'].sum()

        # 3. 依照 Category 字母順序遞增排序，就像按字母排隊
        report = report.sort_values(by='Category')

        # 4. 四捨五入至最接近的整數&轉成 int，就像把小數變整數
        report['Price'] = report['Price'].round().astype(int)

        return report  # 回傳報告

def solve_data_pipeline():  # 主函數
    # 讀取全部輸入
    input_data = sys.stdin.read().split()  # 讀取並分割
    if not input_data:  # 如果沒有，結束
        return

    n = int(input_data[0])  # 記錄數
    records = []  # 列表存記錄
    idx = 1  # 索引

    # 解析輸入資料
    for _ in range(n):  # 循環記錄數
        if idx >= len(input_data): break  # 防止超出
        category = input_data[idx]  # 分類
        item = input_data[idx+1]  # 項目
        price_str = input_data[idx+2]  # 價格字串
        records.append((category, item, price_str))  # 加到記錄
        idx += 3  # 前進

    # 實例化管線&處理資料
    pipeline = DataPipeline(records)  # 創建管線
    final_df = pipeline.process_data()  # 處理

    # 依規定格式輸出
    for index, row in final_df.iterrows():  # 遍歷
        print(f"{row['Category']} {row['Price']}")  # 印出

if __name__ == "__main__":  # 如果直接運行
    solve_data_pipeline()  # 呼叫
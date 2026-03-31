# 這個程式用來處理銷售數據，按地區分組計算總銷售額，並按金額降序排序輸出。
import sys  # 引入sys模組，用來讀取標準輸入
import pandas as pd  # 引入pandas庫，用來處理表格數據

class SalesManager:  # 定義一個類別來管理銷售數據
    def __init__(self, data):  # 初始化方法，接收數據
        # 將傳入的字典清單轉換為 DataFrame，就像把數據放進表格裡
        self.df = pd.DataFrame(data, columns=['Region', 'SalesAmount'])

    def generate_report(self):  # 方法來生成報告
        # 1. 使用 groupby 依地區分組 & 加總銷售額，就像把同地區的銷售加起來
        # as_index=False 可以讓 Region 保持為一般的欄位，方便後續排序
        report = self.df.groupby('Region', as_index=False)['SalesAmount'].sum()

        # 2. 依照總銷售額 (SalesAmount) 進行遞減排序 (ascending=False)，就像把最高的放前面
        # 若銷售額相同，則依照地區名稱遞增排序以保持穩定性
        report = report.sort_values(by=['SalesAmount', 'Region'], ascending=[False, True])

        return report  # 回傳報告

def solve_sales_report():  # 主函數來解決銷售報告問題
    input_data = sys.stdin.read().split()  # 讀取所有輸入並分割成列表
    if not input_data:  # 如果沒有輸入，就結束
        return

    n = int(input_data[0])  # 讀取紀錄筆數 N
    records = []  # 準備一個列表來存記錄
    idx = 1  # 索引從1開始

    # 解析接下來的 N 行資料
    for _ in range(n):  # 循環N次
        region = input_data[idx]  # 地區名稱
        sales = int(input_data[idx+1])  # 銷售額
        records.append({'Region': region, 'SalesAmount': sales})  # 加到記錄裡
        idx += 2  # 索引加2

    # 實例化 SalesManager & 產生報告
    manager = SalesManager(records)  # 創建管理器
    result_df = manager.generate_report()  # 生成報告

    # 依照題目要求格式輸出
    for index, row in result_df.iterrows():  # 遍歷每一行
        print(f"{row['Region']} {row['SalesAmount']}")  # 印出地區和銷售額

if __name__ == "__main__":  # 如果直接運行這個檔案
    solve_sales_report()  # 呼叫主函數
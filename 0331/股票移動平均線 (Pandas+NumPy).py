# 這個程式用來計算股票價格的移動平均線，使用滾動窗口平均。
import sys  # 引入sys模組，用來讀取標準輸入
import pandas as pd  # 引入pandas庫，用來處理時間序列數據
import numpy as np  # 引入numpy庫，用來處理數組

class StockTracker:  # 定義股票追蹤器類別
    def __init__(self, prices, window):  # 初始化，接收價格和窗口
        # 將輸入的列表轉為 Pandas Series，這是時間序列分析的基礎，就像把數據變成序列
        self.prices = pd.Series(prices)
        self.window = window  # 窗口大小

    def calculate_moving_average(self):  # 方法來計算移動平均
        # 1. 使用 rolling().mean() 計算移動平均，就像滑動窗口算平均
        ma = self.prices.rolling(window=self.window).mean()
        # 2. 將前面的 NaN 缺失值替換為 0.0，就像把空的填0
        ma = ma.fillna(0.0)
        return ma  # 回傳

def solve_stock_tracker():  # 主函數
    input_data = sys.stdin.read().split()  # 讀取輸入
    if not input_data:  # 如果沒有，結束
        return

    n = int(input_data[0])  # 價格數
    w = int(input_data[1])  # 窗口

    # 讀取接下來的 N 個整數作為股價
    prices = [int(x) for x in input_data[2:2+n]]  # 讀取價格

    # 實例化追蹤器並計算
    tracker = StockTracker(prices, w)  # 創建追蹤器
    ma_result = tracker.calculate_moving_average()  # 計算平均

    # 依照題目要求：四捨五入到小數點後第 1 位，並以空格分隔
    formatted_output = [f"{x:.1f}" for x in ma_result]  # 格式化
    print(" ".join(formatted_output))  # 印出

if __name__ == "__main__":  # 如果直接運行
    solve_stock_tracker()  # 呼叫
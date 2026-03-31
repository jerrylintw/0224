# 這個程式用來處理影像矩陣，執行旋轉、轉置、乘法等操作，並輸出最終的矩陣。
import sys  # 引入sys模組，用來讀取標準輸入
import numpy as np  # 引入numpy庫，用來處理矩陣運算

class ImageProcessor:  # 定義影像處理器類別
    def __init__(self, matrix):  # 初始化，接收矩陣
        # 轉成 NumPy 陣列以利後續運算，就像把數據變成數組方便操作
        self.matrix = np.array(matrix)

    def rotate(self):  # 方法來旋轉矩陣
        # rot90 預設逆時針，k=-1 代表順時針轉 90 度，就像把紙轉一下
        self.matrix = np.rot90(self.matrix, k=-1)

    def transpose(self):  # 方法來轉置矩陣
        # 矩陣轉置，就像把行變成列
        self.matrix = np.transpose(self.matrix)

    def multiply(self, x):  # 方法來乘以一個數
        # 廣播機制：全元素乘以 x，就像每個數字都乘x
        self.matrix = self.matrix * x

def solve_image_processor():  # 主函數
    input_data = sys.stdin.read().split()  # 讀取輸入
    if not input_data:  # 如果沒有，結束
        return

    r = int(input_data[0])  # 行數
    c = int(input_data[1])  # 列數

    matrix_data = []  # 列表存矩陣
    idx = 2  # 索引

    # 讀取初始矩陣
    for _ in range(r):  # 循環行數
        row = [int(val) for val in input_data[idx:idx+c]]  # 讀取一行
        matrix_data.append(row)  # 加到矩陣
        idx += c  # 前進

    processor = ImageProcessor(matrix_data)  # 創建處理器

    k = int(input_data[idx])  # 操作數
    idx += 1  # 前進

    # 依序執行 K 個指令
    for _ in range(k):  # 循環操作數
        cmd = input_data[idx]  # 命令
        if cmd == "ROTATE":  # 如果是旋轉
            processor.rotate()  # 旋轉
            idx += 1  # 前進
        elif cmd == "TRANSPOSE":  # 如果是轉置
            processor.transpose()  # 轉置
            idx += 1  # 前進
        elif cmd == "MULTIPLY":  # 如果是乘法
            val = int(input_data[idx+1])  # 乘數
            processor.multiply(val)  # 乘
            idx += 2  # 前進2

    # 抓取最終的列數 & 行數
    final_r, final_c = processor.matrix.shape  # 獲取形狀
    print(f"{final_r} {final_c}")  # 印出行列數

    # 印出轉換後的矩陣
    for row in processor.matrix:  # 遍歷行
        print(*(row.tolist()))  # 印出行

if __name__ == "__main__":  # 如果直接運行
    solve_image_processor()  # 呼叫
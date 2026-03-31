# 這個程式用來分析學生分數，計算每位學生的最高分和每個科目的平均分。
import sys  # 引入sys模組，用來讀取標準輸入
import numpy as np  # 引入numpy庫，用來處理數組和數學運算

class ScoreAnalyzer:  # 定義一個類別來分析分數
    def __init__(self, scores):  # 初始化方法，接收分數列表
        # 將輸入的列表轉為 NumPy 矩陣，就像把數據放進數組裡方便計算
        self.scores_array = np.array(scores)

    def get_max_per_student(self):  # 方法來獲取每位學生的最高分
        # axis=1 代表橫向運算（每個學生），就像找每行的最大值
        return np.max(self.scores_array, axis=1)

    def get_avg_per_subject(self):  # 方法來獲取每個科目的平均分
        # axis=0 代表縱向運算（每個科目），就像找每列的平均值
        return np.mean(self.scores_array, axis=0)

def solve_score_analyzer():  # 主函數來解決分數分析問題
    input_data = sys.stdin.read().split()  # 讀取所有輸入並分割
    if not input_data: return  # 如果沒有輸入，就結束

    n = int(input_data[0])  # 學生數
    m = int(input_data[1])  # 科目數

    all_scores = []  # 準備列表存所有分數
    idx = 2  # 索引從2開始
    for _ in range(n):  # 循環學生數
        student_scores = [int(x) for x in input_data[idx : idx + m]]  # 讀取一個學生的分數
        all_scores.append(student_scores)  # 加到列表
        idx += m  # 索引前進

    analyzer = ScoreAnalyzer(all_scores)  # 創建分析器

    # 輸出每位學生最高分
    max_scores = analyzer.get_max_per_student()  # 獲取最高分
    print(*(max_scores.astype(int)))  # 印出，轉為整數

    # 輸出每個科目平均值（四捨五入到小數一位）
    avg_scores = analyzer.get_avg_per_subject()  # 獲取平均分
    formatted_avgs = [f"{round(x, 1):.1f}" for x in avg_scores]  # 格式化
    print(*(formatted_avgs))  # 印出

if __name__ == "__main__":  # 如果直接運行
    solve_score_analyzer()  # 呼叫主函數

import sys

class Score:
    # 類別屬性：國文, 英文, 數學的權重（初始預設為 1） 
    weights = [1.0, 1.0, 1.0]

    def __init__(self, name, chin, eng, math):
        # 記錄學生姓名與三科成績 [cite: 112]
        self.name = name
        self.scores = [chin, eng, math]

    @classmethod
    def setWeight(cls, chin, eng, math):
        # 類別方法：設定三科權重 
        cls.weights = [float(chin), float(eng), float(math)]

    def getFinalScore(self):
        # 實體方法：根據各科加權計算學期成績 [cite: 114]
        total_weighted_score = sum(s * w for s, w in zip(self.scores, self.weights))
        total_hours = sum(self.weights)
        return total_weighted_score / total_hours if total_hours != 0 else 0

def solve_score_system():
    # 使用 split() 讀取所有 token，這能完美避開 EOF 讀取不全的問題
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0]) # 第一個數字是操作次數 [cite: 123, 129]
    students = {}
    current = 1 # 從索引 1 開始處理指令
    
    count = 0
    while count < n and current < len(input_data):
        cmd = input_data[current]
        
        if cmd == "weight":
            # 格式: weight <國> <英> <數> [cite: 124]
            w_c = int(input_data[current+1])
            w_e = int(input_data[current+2])
            w_m = int(input_data[current+3])
            Score.setWeight(w_c, w_e, w_m)
            current += 4
            
        elif cmd == "add":
            # 格式: add <Name> <國> <英> <數> [cite: 117, 125]
            name = input_data[current+1]
            s_c = int(input_data[current+2])
            s_e = int(input_data[current+3])
            s_m = int(input_data[current+4])
            
            if name in students:
                students[name] = Score(name, s_c, s_e, s_m)
                print(f"{name} updated") # 若重複則覆蓋並顯示 updated 
            else:
                students[name] = Score(name, s_c, s_e, s_m)
                print(f"{name} added") # 新資料顯示 added [cite: 127]
            current += 5
            
        elif cmd == "query":
            # 格式: query <Name> [cite: 126]
            name = input_data[current+1]
            if name in students:
                s = students[name]
                final = s.getFinalScore()
                # 輸出格式: Name:國, 英文, 數學, 學期成績(兩位小數) 
                print(f"{name}: {s.scores[0]}, {s.scores[1]}, {s.scores[2]}, {final:.2f}")
            else:
                print(f"{name}: None") # 查無學生顯示 None [cite: 120, 128]
            current += 2
            
        count += 1

if __name__ == "__main__":
    solve_score_system()
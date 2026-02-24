def report_sequence():
    try:
        line = input().split()
        if not line: return
        n, k = map(int, line)
        
        students = list(range(1, n + 1))
        order = []
        idx = 0
        
        while students:
            # 計算下一個要離開的人的索引
            idx = (idx + k - 1) % len(students)
            order.append(str(students.pop(idx)))
            
        print(" ".join(order))
    except EOFError:
        pass

report_sequence() 
#4532
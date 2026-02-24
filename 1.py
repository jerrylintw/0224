# 1. 讀取商品筆數 M 與查詢次數 N 
M, N = map(int, input().split())

products = {}

# 2. 建立商品字典 
for i in range(M):
    # 將每一行的商品名與價格切分開來
    name, price = input().split()
    products[name] = price

# 3. 處理查詢請求 
for j in range(N):
    # 讀取要查詢的名稱，使用 .strip() 確保沒有多餘空白 [cite: 10]
    query_name = input().strip()
    # 題目保證名稱一定存在，直接輸出價格 
    print(products[query_name])
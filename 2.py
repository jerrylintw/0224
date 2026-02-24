class Product:
    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price

def solve_order():
    try:
        n = int(input())
        products = []
        total_amount = 0
        
        for _ in range(n):
            data = input().split()
            name = data[0]
            qty = int(data[1])
            price = int(data[2])
            products.append(Product(name, qty, price))
            total_amount += qty * price
            
        for p in products:
            print(f"{p.name}, #{p.qty}, NT${p.price}")
            
        print(f"Total: NT${total_amount}")
    except EOFError:
        pass

solve_order()
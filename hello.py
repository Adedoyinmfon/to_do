

#print("hello, world")

from tabulate import tabulate

data = [
    ["product", "Price", "Stock"],
    ["Laptop", 999.99, 45], 
    ["Mouse", 24.99, 128],
    ["Keyboard", 49.99, 64],
]

print(tabulate(data, headers="firstrow", tablefmt="grid"))
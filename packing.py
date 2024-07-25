#task1
''' You are given a list of tuples, each representing a customer's order. 
Each tuple contains the customer's name, the product ordered, and the quantity. 
Your task is to unpack each tuple and print the order details in a user-friendly format.
Sample Order Data:

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]
'''

def print_order_details(orders):
    for customer_name, product, quantity in orders: 
        print(f"Customer:{customer_name}, Product: {product}, Quantity: {quantity}")
        
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

print_order_details(orders)
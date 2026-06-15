#Martha Guzman
#Total cost project

def calculate_total(price, quantity):
    total = price * quantity
    return total

item_price = float(input("Enter the item price: "))
item_quantity = int(input("Enter the quantity: "))

final_total = calculate_total(item_price, item_quantity)

print("The total cost is: $", final_total)


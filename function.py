def calculate_total(price, quantity):
    total = price * quantity
    return total


price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = calculate_total(price, quantity)

print("Total bill:", total)

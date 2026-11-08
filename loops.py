table = int(input("Enter the table you want: "))
number = 1
total = 0

while number <= 10:
    print(table, "x", number, "=", table * number)
    total += table * number
    number += 1

print("Total:", total)
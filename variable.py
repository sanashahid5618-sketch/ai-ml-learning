product =(input("enter product name:")) 
price =float(input("enter price:")) 
quantity=int(input("enter total quantity:")) 
discount_percent = float(input("Enter discount percentage: ")) 
subtotal=price * quantity 
Discount = subtotal * discount_percent / 100 
final =subtotal-Discount 
print("subtotal :" , subtotal) 
print(" Discount:" ,  Discount ) 
print("  final " , final  )

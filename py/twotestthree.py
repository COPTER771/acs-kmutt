menu_price = {
    1: 25, 
    2: 30, 
    3: 35 
}
total_price = 0
total_cups = 0
while True:
    menu = int(input())
    if menu == 0:
        break
    qty = int(input())  
    total_price += menu_price[menu] * qty
    total_cups += qty

discount = 0
if total_price >= 300 :
    discount = max(discount, 0.05)


final_price = total_price * (1 - discount)

print(round(final_price))
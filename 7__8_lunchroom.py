pizza_orders = ['peperoni','mangerita','bbq chicken en bacon']
complete_orders=[] 
for order in pizza_orders:
    print("je bestelling ("+order+") is klaar")
    pizza_orders.remove(order)
    complete_orders.append(order) 
print(complete_orders)

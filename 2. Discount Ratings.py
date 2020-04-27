amount = float(input("Enter Sale amount: "))
dis = 0
if amount < 0:
    print("Invalid amount written.")
else:
    if 0 <= amount < 5000:
        dis = 5
    elif 5000 <= amount < 10000:
        dis = 10
    elif 10000 <= amount < 15000:
        dis = 20
    elif 15000 <= amount:
        dis = 30
    discount = (dis/100) * amount
    print("Discount: ", discount)
    net = amount - discount
    print("Net Pay: ", net)

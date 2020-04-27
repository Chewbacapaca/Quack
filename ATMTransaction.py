import random
import string
totalbalance = 0
pin = 0
interestrate = 5
while pin < 1000 or pin > 9999:
    pin = int(input("Enter account PIN: "))
    if 1000 <= pin <= 9999:
        break
    else:
        print("Wrong PIN. Try again.")

while True:
    if 1000 <= pin <= 9999:
        print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit")
        sel = int(input("Enter your selection: "))
        if sel == 1:
            print("Your current balance is ", totalbalance, ".")

        elif sel == 2:
            withdraw_amt = float(input("\nEnter amount to withdraw: "))
            if totalbalance < withdraw_amt:
                print("Sorry, your balance is not enough for withdrawal.")
            else:
                totalbalance -= withdraw_amt
                print("Withdrew", withdraw_amt, "successfully. Updated balance is", totalbalance, ".")

        elif sel == 3:
            deposit_amt = float(input("\nEnter amount to deposit: "))
            totalbalance += deposit_amt
            print("Deposited", deposit_amt, "successfully. Updated balance is", totalbalance, ".")

        elif sel == 4:
            print("\nTransaction is now complete.")
            print("ATM ID: 203")
            transaction_number = str(203)
            transaction_number += ''.join(random.choice(string.digits) for i in range(6))
            print("Transaction number: ", transaction_number)
            print("Current Interest Rate: ", interestrate, end="% p.a.")
            print("\nMonthly Interest Rate: ", interestrate/12, end="%")
            print("\nThanks for choosing us as your bank.")
            exit()

        else:
            print("Invalid selection. Try again.\n")

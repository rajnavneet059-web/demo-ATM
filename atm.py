balance = 100000
pin = 7903
bank_statement=[]       

print("===== ❤️ Welcome to PNB ATM ❤️ =====")

entered_pin = int(input("Enter your PIN: "))
 
if entered_pin == pin:
    while True:
        print("\nplease select an option")
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. deposite")
        print("4. statement")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your balance is:", balance)
            bank_statement.append(f"Checked Balance: {balance}")
        elif choice == 2:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print("Please collect your cash")
                print("you want to check balance prees 1 ")
                bank_statement.append(f"withdraw: {amount} | Balance: {balance}")
            else:
                print("Insufficient balance")
        elif choice == 3:
            amount=(int(input("enter your ammount")))
            balance+=amount
            bank_statement.append(f"Deposit: {amount} | Balance: {balance}")
        elif choice == 4:
            print("\n===== Transaction History =====")
            if len(bank_statement) == 0:
                print("No transactions yet")
            else:
                for record in bank_statement:
                    print(record)
        elif choice == 5:
            print("Thank you for using PNB ATM")
            break
        else:
            print("Invalid choice")

else:
    print("Wrong PIN")
print("=== Welcome to Renu Bank ===")

balance = 1000

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("Your Balance is:", balance)
    
    elif choice == "2":
    amount = int(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Deposited! New Balance:", balance)
    
    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance = balance - amount
          print("Withdrawn! New Balance:", balance)
        else:
            print("Not enough balance!")
    
    elif choice == "4":
        print("Thank you for using Renu Bank!")
        break
    
    else:
        print("Wrong choice, try again")
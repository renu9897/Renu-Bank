print("="*40)
print("      🏦 WELCOME TO RENU BANK ATM 🏦")
print("="*40)

balance = 10000
pin = "1234"

entered_pin = input("Enter your 4 digit PIN: ")

if entered_pin != pin:
    print("❌ Wrong PIN! Card Blocked")
else:
    while True:
        print("\n" + "="*40)
        print("1. 💰 Check Balance")
        print("2. 💵 Deposit Money")
        print("3. 💳 Withdraw Money")
        print("4. 📄 Mini Statement")
        print("5. 🚪 Exit")
        print("="*40)
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print(f"Your Current Balance: ₹{balance}")
            
        elif choice == "2":
            amount = int(input("Enter amount to deposit: ₹"))
            balance += amount
            print(f"✅ ₹{amount} Deposited Successfully")
            print(f"New Balance: ₹{balance}")
            
        elif choice == "3":
            amount = int(input("Enter amount to withdraw: ₹"))
            if amount > balance:
                print("❌ Insufficient Balance")
            else:
                balance -= amount
                print(f"✅ ₹{amount} Withdrawn Successfully")
                print(f"Remaining Balance: ₹{balance}")
                
        elif choice == "4":
            print("📄 Last 3 Transactions:")
            print("1. Deposited ₹5000")
            print("2. Withdrawn ₹2000")
            print(f"3. Current Balance ₹{balance}")
            
        elif choice == "5":
            print("🙏 Thank you! Visit Again")
            print("Please collect your card")
            break
            
        else:
            print("❌ Invalid Choice! Try Again")
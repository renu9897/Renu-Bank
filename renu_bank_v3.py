import json

pin = 1234
entered_pin = int(input("Enter 4 digit PIN: "))

if entered_pin != pin:
    print("Wrong PIN! Access Denied")
    exit()
else:
    print("PIN sahi hai. Welcome to RENU BANK v3")
    
    # Balance file se load karo
    try:
        with open("balance.txt", "r") as f:
            balance = int(f.read())
    except:
        balance = 10000
    
    history = []

    while True:
        print("\n1. Balance Dekho")
        print("2. Paise Jama Karo")
        print("3. Paise Nikalo")
        print("4. Exit")
        print("5. Transaction History Dekho")

        choice = input("Apna option chuno: ")

        if choice == "1":
            print(f"Aapka Balance: ₹{balance}")
        elif choice == "2":
            amount = int(input("Kitne paise jama karne hai: "))
            balance += amount
            history.append(f"Jama: +₹{amount}")
            print(f"₹{amount} jama ho gaye. Naya Balance: ₹{balance}")
        elif choice == "3":
            amount = int(input("Kitne paise nikalne hai: "))
            if amount > balance:
                print("Balance kam hai!")
            else:
                balance -= amount
                history.append(f"Nikala: -₹{amount}")
                print(f"₹{amount} nikal gaye. Naya Balance: ₹{balance}")
        elif choice == "4":
            # Balance file me save karo
            with open("balance.txt", "w") as f:
                f.write(str(balance))
            print("Thank you! Visit Again")
            break
        elif choice == "5":
            print("Transaction History:")
            if len(history) == 0:
                print("Koi transaction nahi hui")
            else:
                for h in history:
                    print(h)
        else:
            print("Galat option!")
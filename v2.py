pin = 1234
entered_pin = int(input("Enter 4 digit PIN: "))

if entered_pin != pin:
    print("Wrong PIN! Access Denied")
    exit()
else:
    print("PIN sahi hai. Welcome to RENU BANK")
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
            print("Tumhara balance:", balance)
            
        elif choice == "2":
            amount = int(input("Kitne paise jama karne hai: "))
            balance = balance + amount
            history.append("Jama kiye: " + str(amount))
            print("Naya balance:", balance)
            
        elif choice == "3":
            amount = int(input("Kitne paise nikalne hai: "))
            balance = balance - amount
            history.append("Nikale: " + str(amount))
            print("Naya balance:", balance)
            
        elif choice == "4":
            print("Dhanyawad! Bank band ho raha hai")
            break
            
        elif choice == "5":
            print("Tumhari History:", history)
            
        else:
            print("Galat option")
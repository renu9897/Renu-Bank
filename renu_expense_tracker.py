expenses = []

print("----- RENU EXPENSE TRACKER -----")

while True:
    print("\n1. Kharcha add karo")
    print("2. Saara hisaab dekho") 
    print("3. Total kharcha")
    print("4. Bahar niklo")
    
    choice = input("Choice: ")
    
    if choice == '1':
        item = input("Kis cheez pe kharcha: ")
        amount = float(input("Kitne rupaye: "))
        expenses.append({"item": item, "amount": amount})
        print("Add ho gaya! ✅")
        
    elif choice == '2':
        print("\nTumhara Hisaab:")
        for i, exp in enumerate(expenses, 1):
            print(i, ".", exp["item"], "-", exp["amount"], "rs")
            
    elif choice == '3':
        total = 0
        for exp in expenses:
            total = total + exp["amount"]
        print("Total Kharcha:", total, "rs")
        
    elif choice == '4':
        print("Bye! Paisa bachao 💰")
        break
    else:
        print("Galat choice!")
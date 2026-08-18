print("=== RENU CALCULATOR ===")
print("1. Jodna +")
print("2. Ghatana -")
print("3. Guna *")
print("4. Bhag /")

while True:
    choice = input("\nKya karna hai 1/2/3/4 ya Exit: ")
    
    if choice == "Exit":
        print("Bye! 💚")
        break
    
    num1 = float(input("Pehla number: "))
    num2 = float(input("Dusra number: "))
    
    if choice == "1":
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == "2":
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == "3":
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == "4":
        if num2 != 0:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("0 se bhag nahi de sakte!")
    else:
        print("Galat option!")
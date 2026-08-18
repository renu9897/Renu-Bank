import json

# Sab users ka data is file me save hoga
DATA_FILE = "users.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

users = load_data()

while True:
    print("\n===== RENU BANK v4 =====")
    print("1. Naya Account Banao")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Option chuno: ")
    
    if choice == "1":
        name = input("Naam likho: ")
        pin = input("4 digit PIN set karo: ")
        if name in users:
            print("Ye naam pehle se hai!")
        else:
            users[name] = {"pin": pin, "balance": 10000, "history": []}
            save_data(users)
            print(f"{name} ka account ban gaya! Balance: ₹10000")
    
    elif choice == "2":
        name = input("Naam likho: ")
        pin = input("PIN likho: ")
        
        if name in users and users[name]["pin"] == pin:
            print(f"Welcome {name}!")
            while True:
                print("\n1. Balance")
                print("2. Paise Jama")
                print("3. Paise Nikalo")
                print("4. Transfer")
                print("5. History")
                print("6. Logout")
                
                op = input("Option: ")
                
                if op == "1":
                    print(f"Balance: ₹{users[name]['balance']}")
                elif op == "2":
                    amt = int(input("Kitne jama karne: "))
                    users[name]["balance"] += amt
                    users[name]["history"].append(f"Jama: +₹{amt}")
                    save_data(users)
                    print(f"Naya Balance: ₹{users[name]['balance']}")
                elif op == "3":
                    amt = int(input("Kitne nikalne: "))
                    if amt > users[name]["balance"]:
                        print("Balance kam hai")
                    else:
                        users[name]["balance"] -= amt
                        users[name]["history"].append(f"Nikala: -₹{amt}")
                        save_data(users)
                        print(f"Naya Balance: ₹{users[name]['balance']}")
                elif op == "4":
                    to_user = input("Kisko bhejne hai: ")
                    if to_user in users:
                        amt = int(input("Kitne transfer karne: "))
                        if amt > users[name]["balance"]:
                            print("Balance kam hai")
                        else:
                            users[name]["balance"] -= amt
                            users[to_user]["balance"] += amt
                            users[name]["history"].append(f"Transfer: -₹{amt} to {to_user}")
                            users[to_user]["history"].append(f"Transfer: +₹{amt} from {name}")
                            save_data(users)
                            print("Transfer ho gaya!")
                    else:
                        print("User nahi mila")
                elif op == "5":
                    print("History:")
                    for h in users[name]["history"]:
                        print(h)
                elif op == "6":
                    break
        else:
            print("Galat naam ya PIN!")
    
    elif choice == "3":
        print("Thank you!")
        break
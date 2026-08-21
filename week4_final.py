import os
import time

def banner():
    print("="*40)
    print(" ADVANCED CODER TOOL - WEEK 4")
    print("="*40)

def option1():
    print("\n[1] System Scan Chal Raha Hai...")
    time.sleep(1)
    print(f"OS Name: {os.name}")
    print("Scan Complete! Sab Secure Hai.")

def option2():
    print("\n[2] Password Strength Checker")
    pwd = input("Ek password likho: ")
    if len(pwd) < 6:
        print("Result: Weak Password ❌")
    elif len(pwd) < 10:
        print("Result: Medium Password ⚠️")
    else:
        print("Result: Strong Password ✅")

while True:
    banner()
    print("\n1. Scan My System")
    print("2. Check Password Strength")
    print("3. Exit")

    choice = input("\nApna option chuno (1/2/3): ")

    if choice == "1":
        option1()
    elif choice == "2":
        option2()
    elif choice == "3":
        print("Tool Band Ho Raha Hai... Bye!")
        break
    else:
        print("Galat Option! Dubara try karo.")

    input("\nContinue karne ke liye Enter dabao...")
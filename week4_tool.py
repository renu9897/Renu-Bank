import os
import time

def banner():
    print("="*40)
    print(" RENU - ADVANCED TOOL WEEK 4")
    print("="*40)

def option1():
    print("\n[1] System Scanner")
    print(f"System Name: {os.name}")
    try:
        files = os.listdir(".")
        print(f"Is folder me {len(files)} files hai:")
        for f in files[:10]:
            print(f" - {f}")
        print("\nScan Complete ✅")
    except Exception as e:
        print("Error:", e)

def option2():
    print("\n[2] Password Strength Checker")
    pwd = input("Ek password likho: ")
    score = 0
    if len(pwd) >= 6: score += 1
    if any(c.isdigit() for c in pwd): score += 1
    if any(c.isupper() for c in pwd): score += 1

    if score == 3:
        print("Result: STRONG Password ✅")
    elif score == 2:
        print("Result: MEDIUM Password ⚠️")
    else:
        print("Result: WEAK Password ❌")

# --- MAIN PROGRAM ---
while True:
    banner()
    print("\n1. Scan My Folder (Automation)")
    print("2. Password Checker")
    print("3. Exit Tool")

    choice = input("\nOption chuno (1/2/3): ")

    if choice == "1":
        option1()
    elif choice == "2":
        option2()
    elif choice == "3":
        print("\nBye Renu! Tool band ho raha hai...")
        break
    else:
        print("Galat option!")

    print("\n" + "-"*40)
    input("Continue karne ke liye ENTER dabao...")
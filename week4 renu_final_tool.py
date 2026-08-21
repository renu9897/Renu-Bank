import os
import time

def banner():
    print("\n" + "="*40)
    print(" RENU FINAL HACKING TOOL - WEEK 4")
    print("="*40)

def automation_scan():
    print("\n[Automation] Folder Auto Scan...")
    files = os.listdir(".")
    print(f"Total Files Found: {len(files)}")
    time.sleep(1)
    print("Scan Done ✅")

def brute_logic():
    print("\n[Brute Force Logic] Demo")
    pwd = input("Target password guess karo: ")
    # Ye sirf LOGIC dikhane ke liye hai - real hacking nahi
    common = ["123456", "password", "renu123", "admin"]
    if pwd in common:
        print(f"Password '{pwd}' weak hai, guess ho gaya! ⚠️")
    else:
        print(f"Password '{pwd}' strong hai, guess nahi hua ✅")

while True:
    banner()
    print("\n1. Scan (Automation)")
    print("2. Attack (Brute Force Logic)")
    print("3. Exit")

    c = input("\nOption chuno: ")
    if c == "1":
        automation_scan()
    elif c == "2":
        brute_logic()
    elif c == "3":
        print("\nTool Exit... Bye Renu!")
        break
    else:
        print("Galat Option!")

    input("\nContinue ke liye ENTER...")

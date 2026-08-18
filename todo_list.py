print("=== RENU TODO LIST ===")

tasks = []

while True:
    print("\n1. Kaam Add karo")
    print("2. Kaam Dekho")
    print("3. Kaam Complete karo")
    print("4. Kaam Delete karo")
    print("5. Exit")
    
    choice = input("Option chuno: ")
    
    if choice == "1":
        task = input("Kaunsa kaam add karna hai: ")
        tasks.append({"kaam": task, "status": "Pending"})
        print(f"'{task}' add ho gaya!")
    
    elif choice == "2":
        if len(tasks) == 0:
            print("Koi kaam nahi hai")
        else:
            print("\n--- Tumhare Kaam ---")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t['kaam']} - {t['status']}")
    
    elif choice == "3":
        num = int(input("Kaunsa number complete hua: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["status"] = "Completed ✅"
            print("Shabash! Kaam complete ho gaya")
        else:
            print("Galat number")
    
    elif choice == "4":
        num = int(input("Kaunsa number delete karna: "))
        if 1 <= num <= len(tasks):
            deleted = tasks.pop(num-1)
            print(f"'{deleted['kaam']}' delete ho gaya")
        else:
            print("Galat number")
    
    elif choice == "5":
        print("Bye! Kaam karte raho 💪")
        break
    
    else:
        print("Galat option!")
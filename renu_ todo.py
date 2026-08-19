tasks = []

print("----- RENU TO-DO LIST -----")

while True:
    print("\n1. Task add karo")
    print("2. Saare task dekho")
    print("3. Task delete karo")
    print("4. Bahar niklo")
    
    choice = input("Choice likho 1/2/3/4: ")
    
    if choice == '1':
        task = input("Naya task likho: ")
        tasks.append(task)
        print("Task add ho gaya! ✅")
        
    elif choice == '2':
        print("\nTumhare Tasks:")
        for i, task in enumerate(tasks, 1):
            print(i, ".", task)
            
    elif choice == '3':
        num = int(input("Kaunsa number delete karna hai: "))
        tasks.pop(num-1)
        print("Task delete ho gaya! 🗑️")
        
    elif choice == '4':
        print("Bye Renu!")
        break
    else:
        print("Galat choice!")
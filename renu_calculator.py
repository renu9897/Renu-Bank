print("----- RENU CALCULATOR -----")

num1 = float(input("Pehla number likho: "))
num2 = float(input("Dusra number likho: "))

print("\n1. Jod  +")
print("2. Ghata -")
print("3. Guna  *")
print("4. Bhag  /")

choice = input("Kya karna hai? 1/2/3/4: ")

if choice == '1':
    print("Jawab:", num1 + num2)
elif choice == '2':
    print("Jawab:", num1 - num2)
elif choice == '3':
    print("Jawab:", num1 * num2)
elif choice == '4':
    print("Jawab:", num1 / num2)
else:
    print("Galat choice!")

print("Calculator band")
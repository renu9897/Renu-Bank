import random

print("----- RENU GUESSING GAME -----")
print("1 se 100 ke beech number socha hai. Guess karo!")

number = random.randint(1, 100)
guess = 0

while guess != number:
    guess = int(input("Apna guess likho: "))
    
    if guess < number:
        print("Bahut chota hai! Bada number bolo ⬆️")
    elif guess > number:
        print("Bahut bada hai! Chota number bolo ⬇️")
    else:
        print("Wah! Sahi pakda 🎉 Number tha:", number)
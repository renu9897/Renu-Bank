import random

print("=== RENU KA NUMBER GUESSING GAME ===")
print("Computer ne 1 se 100 ke beech ek number socha hai")
print("Tumhe guess karna hai!")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("\nApna guess batao: "))
    attempts = attempts + 1
    
    if guess == secret_number:
        print(f"SHABASH! Tumne sahi pakad liya 🎉")
        print(f"Tumne {attempts} try me jeet liya")
        break
    
    elif guess < secret_number:
        print("Thoda bada number bolo ⬆️")
    
    elif guess > secret_number:
        print("Thoda chota number bolo ⬇️")
    
    if attempts == 10:
        print(f"10 try khatam! Sahi jawab tha: {secret_number}")
        print("Koi baat nahi, dobara khelo 💪")
        break
import random

print("="*30)
print("    🎮 WELCOME TO NUMBER GAME 🎮")
print("    Guess the number 1 to 100")
print("="*30)

secret = random.randint(1, 100)
attempts = 0
score = 100

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess == secret:
        print(f"🎉 CORRECT! You won in {attempts} attempts!")
        print(f"Your Score: {score}")
        break
    elif guess < secret:
        print("⬆️ Too Low! Try Higher")
        score -= 10
    else:
        print("⬇️ Too High! Try Lower")
        score -= 10
    
    if score < 0:
        score = 0

print("Thanks for playing!")
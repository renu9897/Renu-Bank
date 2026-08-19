import random

print("----- RENU OTP GENERATOR -----")

# 4 digit OTP
otp = random.randint(1000, 9999)
print("Tumhara OTP hai:", otp)

# 6 digit OTP bhi bana sakte hain
otp6 = random.randint(100000, 999999)
print("6 Digit OTP:", otp6)

print("Note: Har baar naya OTP aayega")
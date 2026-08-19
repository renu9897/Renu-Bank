print("----- RENU PASSWORD CHECKER -----")

password = input("Password likho check karne ke liye: ")

length = len(password)
has_number = False
has_upper = False

for char in password:
    if char.isdigit():
        has_number = True
    if char.isupper():
        has_upper = True

print("\n--- REPORT ---")
if length >= 8:
    print("✅ Length thik hai")
else:
    print("❌ Kam se kam 8 character hone chahiye")

if has_number:
    print("✅ Number hai")
else:
    print("❌ 1 number add karo")

if has_upper:
    print("✅ Capital letter hai")
else:
    print("❌ 1 Capital letter add karo")

if length >= 8 and has_number and has_upper:
    print("\n🔥 Password Strong hai!")
else:
    print("\n😅 Password Weak hai. Strong banao")
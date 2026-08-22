# RENU BANK - 3 Level Secure Login System
# Project: Week 4 - Made by Renu

print("====== Welcome to Renu Bank - Secure Login ======")

# Step 1 - OTP Verification
otp = input("\nStep 1/3 - Enter OTP (123456): ")
if otp != "123456":
    print("❌ Wrong OTP - Login Failed")
    exit()
print("✅ OTP Verified!")

# Step 2 - QR Code Verification
qr = input("\nStep 2/3 - Enter QR Code (2025): ")
if qr != "2025":
    print("❌ Wrong QR - Login Failed")
    exit()
print("✅ QR Verified!")

# Step 3 - Face Verification
face = input("\nStep 3/3 - Enter Face ID (123): ")
if face != "123":
    print("❌ Face Not Matched - Login Failed")
    exit()

print("\n===============================")
print("✅ LOGIN SUCCESS")
print("Welcome to Renu Bank, Renu!")
print("===============================")
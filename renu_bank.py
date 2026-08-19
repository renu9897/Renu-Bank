# Renu Bank - Login System
users = {} # Dictionary me username : password

# 1. Account banana
username = input("Naya account banao - Naam likho: ")
password = input("Password rakho: ")
users[username] = password

# File me save karna
file = open("users.txt", "a")
file.write(username + "," + password + "\n")
file.close()
print("Account ban gaya! ✅")

# 2. Login karna
print("\n--- LOGIN KARO ---")
try:
    login_user = input("Username: ")
    login_pass = input("Password: ")

    if users[login_user] == login_pass:
        print("Login Successful! Welcome", login_user)
    else:
        print("Password galat hai 😅")
except:
    print("Ye username mila hi nahi!")
import os

print("----- RENU FILE ORGANIZER -----")

# Is folder ki saari files check karega
folder = input("Kaunsa folder organize karna hai? Path likho: ")

files = os.listdir(folder)

for file in files:
    if file.endswith(".jpg") or file.endswith(".png"):
        new_folder = "Images"
    elif file.endswith(".pdf"):
        new_folder = "PDFs"
    elif file.endswith(".py"):
        new_folder = "Python_Files"
    else:
        new_folder = "Others"
    
    # Folder banega agar nahi hai to
    if not os.path.exists(os.path.join(folder, new_folder)):
        os.mkdir(os.path.join(folder, new_folder))
    
    print(file, "->", new_folder, "me gaya")

print("\nKaam khatam! Files organize ho gayin ✅")
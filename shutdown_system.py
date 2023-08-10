import os

def restart_pc():
    os.system("shutdown /r /t 0")

def shutdown_pc():
    os.system("shutdown /s /t 0")

def logout_pc():
    os.system("shutdown /l")

print("1. Restart PC")
print("2. Shutdown PC")
print("3. Logout PC")

choice = input("Enter your choice (1-3): ")

if choice == '1':
    restart_pc()
elif choice == '2':
    shutdown_pc()
elif choice == '3':
    logout_pc()
else:
    print("Invalid choice.")

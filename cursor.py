import os
name = input("Enter your name: ")
print(f"Hello {name}")
place = input("where are you studying: ")
print(f"you are studying in {place}")

while True:
    password = input("create password: ")
    pass_word = any(char.isdigit() for char in password)
    at = "@" in password
    if pass_word and at:
        os.system('cls')
        confirm_password = input("confirm password: ")
        if confirm_password == password:
            print("Password set successfully!")
            break
        else:
            print("Passwords do not match. Please try again.")
    else:
        print(
            "Password must contain at least one digit and an @ symbol. Please try again.")

import re
import random
import string

history = []

common_passwords = [
    "123456", "password", "admin", "qwerty",
    "abc123", "welcome", "letmein", "password123"
]

def calculate_score(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 20
    else:
        suggestions.append("Increase password length.")

    if re.search(r"[A-Z]", password):
        score += 20
    else:
        suggestions.append("Add uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 20
    else:
        suggestions.append("Add lowercase letter.")

    if re.search(r"\d", password):
        score += 20
    else:
        suggestions.append("Add numbers.")

    if re.search(r"[!@#$%^&*()_+=]", password):
        score += 20
    else:
        suggestions.append("Add special characters.")

    return score, suggestions

def strength(score):
    if score == 100:
        return "Very Strong"
    elif score >= 80:
        return "Strong"
    elif score >= 60:
        return "Medium"
    elif score >= 40:
        return "Weak"
    return "Very Weak"

def crack_time(score):
    if score == 100:
        return "1000+ Years"
    elif score >= 80:
        return "100 Years"
    elif score >= 60:
        return "1 Year"
    elif score >= 40:
        return "1 Week"
    return "Few Seconds"

def generate_password(length):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password

def analyze(password):
    score, suggestions = calculate_score(password)

    print("\n========== PASSWORD REPORT ==========")
    print("Password :", password)
    print("Length   :", len(password))
    print("Score    :", score, "/100")
    print("Strength :", strength(score))
    print("Crack Time :", crack_time(score))

    if password.lower() in common_passwords:
        print("Warning : Common Password!")

    if suggestions:
        print("\nSuggestions:")
        for s in suggestions:
            print("-", s)
    else:
        print("Excellent Password!")

    history.append(password) 
def security_tips():
    print("\n========== SECURITY TIPS ==========")
    print("1. Use 12+ character password.")
    print("2. Use uppercase and lowercase letters.")
    print("3. Include numbers and symbols.")
    print("4. Never reuse old passwords.")
    print("5. Enable Two-Factor Authentication.")

while True:

    print("\n==============================")
    print(" PASSWORD STRENGTH CHECKER ")
    print("==============================")
    print("1. Check Password")
    print("2. Generate Password")
    print("3. View Password History")
    print("4. Security Tips")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        password = input("Enter Password: ")
        analyze(password)

    elif choice == "2":

        length = input("Enter Password Length: ")

        if length.isdigit():

            new_password = generate_password(int(length))
            print("\nGenerated Password:", new_password)

            score, _ = calculate_score(new_password)
            print("Strength:", strength(score))

        else:
            print("Please enter a valid number.")

    elif choice == "3":

        print("\n========== HISTORY ==========")

        if len(history) == 0:
            print("No passwords checked yet.")

        else:

            for index, item in enumerate(history, start=1):

                score, _ = calculate_score(item)

                print(
                    str(index) + ".",
                    item,
                    "-",
                    strength(score)
                )

    elif choice == "4":

        security_tips()

    elif choice == "5":

        print("\nSaving history...")

        with open("history.txt", "w") as file:

            for item in history:
                file.write(item + "\n")

        print("History saved in history.txt")
        print("Thank you for using Password Strength Checker.")
        break

    else:

        print("Invalid choice. Try again.")

print("\n========== PROJECT FINISHED ==========")
print("Cyber Security Mini Project")
print("Password Strength Checker")
print("Developed in Python")

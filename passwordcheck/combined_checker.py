import re
import hashlib
import requests

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return "Weak: Include at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Weak: Include at least one lowercase letter."
    if not re.search(r'[0-9]', password):
        return "Weak: Include at least one number."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: Include at least one special character."
    return "Strong: Your password is secure."

def check_password_in_breach(password):
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    if suffix in response.text:
        return "Breached: Your password has been found in a data breach. Avoid using it!"
    return "Safe: Password not found in breach database."

if __name__ == "__main__":
    password = input("Enter a password to check: ")
    strength = check_password_strength(password)
    breach_status = check_password_in_breach(password)

    print(f"Password Strength: {strength}")
    print(f"Breach Status: {breach_status}")

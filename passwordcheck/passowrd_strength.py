import re

def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."

    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        return "Weak: Include at least one uppercase letter."

    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        return "Weak: Include at least one lowercase letter."

    # Check for numbers
    if not re.search(r'[0-9]', password):
        return "Weak: Include at least one number."

    # Check for special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: Include at least one special character."

    return "Strong: Your password is secure."

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to test its strength: ")
    result = check_password_strength(password)
    print(result)

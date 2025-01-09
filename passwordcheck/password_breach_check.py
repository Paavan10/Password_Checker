import hashlib
import requests

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
    password = input("Enter a password to check against breach database: ")
    result = check_password_in_breach(password)
    print(result)

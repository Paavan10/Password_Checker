import tkinter as tk
from tkinter import messagebox
import re
import hashlib
import requests

# Function to check password strength
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return "Weak: Include at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Weak: Include at least one lowercase letter."
    if not re.search(r'[0-9]', password):
        return "Weak: Include at least one number."
    if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        return "Weak: Include at least one special character."
    return "Strong: Your password is secure."

# Function to check if the password is in a breach
def check_password_in_breach(password):
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    if suffix in response.text:
        return "Breached: Your password has been found in a data breach. Avoid using it!"
    return "Safe: Password not found in breach database."

# Function to evaluate the password
def evaluate_password():
    password = entry.get()
    if not password.strip():
        messagebox.showwarning("Error", "Please enter a password!")
        return
    
    strength = check_password_strength(password)
    breach_status = check_password_in_breach(password)
    messagebox.showinfo("Password Evaluation", f"{strength}\n{breach_status}")

# GUI setup
root = tk.Tk()
root.title("Password Strength & Breach Checker")

tk.Label(root, text="Enter Password:").pack(pady=5)
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

tk.Button(root, text="Check Password", command=evaluate_password).pack(pady=10)

root.mainloop()

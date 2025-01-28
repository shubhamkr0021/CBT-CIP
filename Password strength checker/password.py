import re
import requests
import hashlib

def assess_password_security(password):

    score = 0
    suggestions = []

    length = len(password)
    if length >= 18:
        score += 40
    elif length >= 12:
        score += 30
    elif length >= 8:
        score += 20
    else:
        suggestions.append("Password should be at least 8 characters")

    if any(c.islower() for c in password):
        score += 15
    else:
        suggestions.append("Include lowercase characters (a-z).")

    if any(c.isupper() for c in password):
        score += 15
    else:
        suggestions.append("Include uppercase characters (A-Z).")

    if any(c.isdigit() for c in password):
        score += 15
    else:
        suggestions.append("Include numbers (0-9).")

    special_chars = set("!@#$%^&*()_+=-`~[]\{}|;':\",./<>?")
    if any(c in special_chars for c in password):
        score += 15
    else:
        suggestions.append("Include special characters (e.g., !@#$%^&*).")

    if is_password_compromised(password):
        suggestions.append("This password has been found in data breaches.  Do NOT use it!")
        score = 0 

    # Overall assessment
    percentage = (score / 100) * 100

    if percentage < 40:
        strength = "Very Weak"
    elif percentage < 60:
        strength = "Weak"
    elif percentage < 80:
        strength = "Moderate"
    else:
        strength = "Strong"

    if not suggestions and strength != "Very Weak":
        suggestions.append("Password strength is good.")


    return strength, percentage, suggestions


def is_password_compromised(password):
    """Checks if a password has been compromised via the HIBP API."""

    try:
        hashed_password = hashlib.sha1(password.encode()).hexdigest().upper()
        prefix = hashed_password[:5]
        url = f"https://api.pwnedpasswords.com/range/{prefix}"

        response = requests.get(url)
        response.raise_for_status() 

        for line in response.text.splitlines():
            suffix, _ = line.split(":") 
            if hashed_password[5:] == suffix:
                return True 

        return False  # Password not found

    except requests.exceptions.RequestException as e:
        print(f"Error checking HIBP API: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


password = input("Enter a password to evaluate: ")
strength, percentage, suggestions = assess_password_security(password)

print(f"Password Strength: {strength} ({percentage:.1f}%)")
for suggestion in suggestions:
    print(f"- {suggestion}")
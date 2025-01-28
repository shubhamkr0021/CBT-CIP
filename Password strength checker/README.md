# Password Strength Checker

This Python script evaluates the strength of a password based on several criteria, including length, character types, and checks against known compromised passwords using the "Have I Been Pwned" (HIBP) API. It provides feedback and suggestions for improving weak passwords.

**Disclaimer:** This script is for educational purposes only. While it incorporates checks against known compromised passwords, it does not guarantee absolute password security. Password strength evaluation is complex, and no single tool can provide a definitive assessment.  Use this script responsibly and ethically. Do not attempt to use it for any unauthorized activity.

## Features

*   Evaluates password strength based on length, lowercase/uppercase letters, numbers, and special characters.
*   Provides specific feedback and suggestions for improving weak passwords.
*   Checks if the password has been compromised using the "Have I Been Pwned" API.
*   Provides a strength rating (Very Weak, Weak, Moderate, Strong) and a percentage score.

## Requirements

*   Python 3.x
*   `requests` library (for interacting with the HIBP API): `pip install requests`

## How to Use

1.  **Clone or Download:** Clone the repository (if you downloaded it as a zip) or download the `password_checker.py` file.
2.  **Install `requests`:** If you don't have the `requests` library installed, open a terminal or command prompt and run: `pip install requests`
3.  **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the file, and run:

    ```bash
    python password_checker.py
    ```

4.  **Enter Password:** The script will prompt you to enter a password.
5.  **View Results:** The script will display the password strength, percentage score, and any suggestions for improvement.

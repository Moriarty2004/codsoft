import random
import string

def generate_password(length=12):
    """Generates a simple random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        user_input = input("Enter the desired password length (default is 12): ")
        length = int(user_input) if user_input else 12
        if length < 1:
            raise ValueError("Password length must be at least 1.")
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")

import random
import string


def generate_password(length=14):
    """
    Generate a random password containing only letters and digits.

    Args:
        length (int): The length of the password, maximum 14.

    Returns:
        str: The generated password.
    """
    if length > 14:
        length = 14
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(length))
    return password


if __name__ == "__main__":
    pw_length = input("Enter password length (max 14): ")
    try:
        pw_length = int(pw_length)
    except ValueError:
        print("Invalid input, using default length 14.")
        pw_length = 14
    if pw_length > 14 or pw_length <= 0:
        print("Invalid length, using max length 14.")
        pw_length = 14
    generated_password = generate_password(pw_length)
    print(f"Generated password: {generated_password}")
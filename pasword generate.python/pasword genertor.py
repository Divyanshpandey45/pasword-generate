import random
import string

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_special=True):
    """Generate a random password."""
    # Define the character sets to choose from
    character_sets = []
    if use_lowercase:
        character_sets.append(string.ascii_lowercase)
    if use_uppercase:
        character_sets.append(string.ascii_uppercase)
    if use_digits:
        character_sets.append(string.digits)
    if use_special:
        character_sets.append(string.punctuation)

    if not character_sets:
        raise ValueError("At least one character type must be selected")

    # Combine all the character sets into one
    all_characters = ''.join(character_sets)

    # Ensure the password contains at least one character from each selected set
    password = [
        random.choice(string_set) for string_set in character_sets
    ]

    # Fill the rest of the password length with random choices from the combined set
    password += [random.choice(all_characters) for _ in range(length - len(password))]

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)

# User input for password length and complexity
length = int(input("Enter the desired password length: "))
use_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

# Generate and print the password
try:
    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special)
    print(f"Generated password: {password}")
except ValueError as e:
    print(e)
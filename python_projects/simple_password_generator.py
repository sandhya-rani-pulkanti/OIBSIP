import string
import random

# Prompt user to enter a valid password length
def get_password_length():
    while True:
        try:
            plen = int(input("Enter the desired password length (positive integer): "))
            if plen > 0:
                return plen
            else:
                print("Please enter a number greater than zero.")
        except ValueError:
            print("That's not a number! Please enter a positive integer.")

# Allow user to select character types for the password
def get_character_types():
    character_types = {
        'letters': False,
        'digits': False,
        'symbols': False
    }
    
    while True:
        print("\nSelect character types for your password:")
        print("1. Letters (A-Z, a-z)")
        print("2. Digits (0-9)")
        print("3. Symbols (e.g., !, @, #, etc.)")
        print("4. Done (Finish selection)")

        choices = input("Enter your choices separated by commas (e.g., 1,2,3): ").split(',')
        
        for choice in choices:
            choice = choice.strip()
            if choice == '1':
                character_types['letters'] = True
            elif choice == '2':
                character_types['digits'] = True
            elif choice == '3':
                character_types['symbols'] = True
            elif choice == '4':
                if any(character_types.values()):
                    return character_types
                else:
                    print("Please select at least one character type before proceeding.")
                    break
            else:
                print(f"Invalid option '{choice}'. Please enter 1, 2, 3, or 4.")
            
# Generate the password based on the user's selections
def generate_password(plen, character_types):
    characters = []
    
    if character_types['letters']:
        characters.extend(string.ascii_letters)  # Adds both lowercase and uppercase letters
    if character_types['digits']:
        characters.extend(string.digits)  # Adds digits 0-9
    if character_types['symbols']:
        characters.extend(string.punctuation)  # Adds punctuation symbols

    # If no character types were selected, return None
    if not characters:
        print("No character types were selected, so no password can be generated.")
        return None

    # Generate password by selecting random characters up to the desired length
    password = ''.join(random.choice(characters) for _ in range(plen))
    return password

# Main program execution
if __name__ == "__main__":
    plen = get_password_length()
    character_types = get_character_types()
    password = generate_password(plen, character_types)
    
    if password:
        print("\nYour generated password is:")
        print(password)

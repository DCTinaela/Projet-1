import sys  # The sys module for system-related operations.
from colorama import Fore, init  # Import the colorama for colored text

init()  # Initialize the colorama library for colored text.


# Prompt the user to enter the text to be encrypted
text_to_encrypt = input(f"{Fore.GREEN}[?] Please Enter your text/message: ")
# Prompt the user to specify the shift length (the key).
key = int(input(f"{Fore.GREEN}[?] Please specify the shift length: "))
# Check if the specified key is within a valid range (0 to 25).
if key > 25 or key < 0:
    # Display an error message if the key is out of range.
    print(f"{Fore.RED}[!] Your shift length should be between 0 and 25 ")
    sys.exit()  # Exit the program if the key is invalid.


message = text_to_encrypt


key = 3
decrypt=True
result = ""
# Iterate through each character in the user's input message.
for character in message:
    # Check if the character is an alphabet letter.
    if character.isalpha():
        # Determine the shift amount based. i.e the amount of times to be shifted e.g 2,3,4....
        shift = key if not decrypt else -key
        # Check if the character is a lowercase letter.
        if character.islower():
            # Apply Caesar cipher transformation for lowercase letters.
            result += chr(((ord(character) - ord('a') + shift) % 26) + ord('a'))
        else:
            # Apply Caesar cipher transformation for uppercase letters.
            result += chr(((ord(character) - ord('A') + shift) % 26) + ord('A'))
    else:
        # Preserve non-alphabet characters as they are.
        result += character
# Encrypt the user's input using the specified key.
encrypted_text = result

# Display the encrypted text.
print(f"{Fore.GREEN}[+] {text_to_encrypt} has been encrypted as {Fore.RED}{encrypted_text}")
# This is not needed at all, this is only for the UI. If you remove the import, make sure to remove the sleep function
from time import sleep

# Setting variables:
# input_text holds the text to be encrypted
# cipher_num holds the offset for each character to be shifted. Ex: an offset of 3 returns each character + 3
input_text = input("Enter a text to be encrypted: \n")
cipher_num = int(input("Enter the integer to cipher: \n"))


# Get a single character, add an offset and returns the equivalent character
# Example: encrypt_character(a, 3) returns d
def encrypt_character(character, offset):
    temp_char = ord(character) + offset
    return chr(temp_char)

# Loops through each character in the input and applies the offset function accordingly
def change_chars(input_text, cipher_num):
    # Making the UI more welcoming
    print("Encrypting...\n")
    sleep(1.5)

    # Empty array that will hold the added numbers later on
    added_ascii_array = []

    # Transform input to array of chars
    input_text_array = list(input_text)

    # For each char, get its ASCII number and add cipher_number
    for char in input_text_array:
        added_ascii_array.append(encrypt_character(char, cipher_num))

    # Converting back to string
    final_array = ''.join(added_ascii_array)

    print('Done! Encrypted message: \n')
    print(final_array)

if "__main__":
    change_chars(input_text, cipher_num)
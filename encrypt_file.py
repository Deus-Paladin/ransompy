import os

# Opens a file, reads the content and encrypts it with the Caesar Cipher and its chosen offset value
def encrypt_file(filepath, offset):
    final_data = []
    with open(filepath, 'r+') as target_file:
        # Rading file data and putting it as an array
        file_data = list(target_file.readlines())

        # Strip leading and trailing spaces
        stripped_file_data = []
        for line in file_data:
            stripped_file_data.append(line.strip())

        # Iterate through each character for each line and encode the character
        for line in stripped_file_data:
            for char in line:
                final_data.append(encrypt_character(char, offset))

        encrypted_data = ''.join(final_data)

        # Puts the file pointer at the beginning of the file, write the encrypted data, truncates (reset the pointer) and closes the file
        target_file.seek(0)
        target_file.write(encrypted_data)
        target_file.truncate()
        target_file.close()

    
    print(f"File {target_file.name} successfully encrypted! \n\nFinal result: {encrypted_data}")

# TODO: next step is to find the file in the system. We need to assume that we don't know the file names

# Function to search for files and returns a list with the names
# def find_filenames():
#     files_list = []
#     os


# Main Caesar Cipher logic
def encrypt_character(character, offset):
    temp_char = ord(character) + offset
    return chr(temp_char)


if "__main__":
    #encrypt_file('../utils/flag.txt', 3)
    print(os.getcwd())

    # 1. change working directory to a common one (in this case, wsl_dev)
    # 2. search for common directories (in this caste, we search for UTILS folder)
    # 3. get all the files inside the directory
    # 4. put the names in our list
    # 5. encrypt everything!
    os.chdir('..')
    print(os.getcwd())
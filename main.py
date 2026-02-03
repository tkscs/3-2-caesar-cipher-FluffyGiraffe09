
import string

alphabet = string.ascii_lowercase

plaintext = "this is a secret message"

key = 3
# Initialize your ciphertext an empty string
ciphertext = ""
for character in plaintext:
    if character == " ":
        encrypted_character = " "
        ciphertext += encrypted_character 
    elif character == "z":
        index = alphabet.index(f"{character}")
        new_index = index - key
        encrypted_character = alphabet[new_index]
        ciphertext += encrypted_character 
    else:
        index = alphabet.index(f"{character}")
        new_index = index + key
        encrypted_character = alphabet[new_index]
        ciphertext += encrypted_character 

print(f"{ciphertext = }")
#caesar encrypt and decrypt
def caesar(message, offset,direction=1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        if char == ' ':
            final_message += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message

def encrypt_caesar(message, offset):
    return caesar(message, offset)

def decrypt_caesar(message, offset):
    return caesar(message, offset,-1)

#vigenere encrypt and decrypt
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt_vigenere(message, key):
    return vigenere(message, key)
    
def decrypt_vigenere(message, key):
    return vigenere(message, key, -1)

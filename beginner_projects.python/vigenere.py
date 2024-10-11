text = 'Hello Zaira'
custom_key = 'python'


def vigenere(message, key, direction):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():

        # Append space to the message
        if char == ' ':
            encrypted_text += char
        elif char in alphabet:  # Make sure to only process alphabet characters
            # Find the right key character to encode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.index(char)

            # Calculate the new index by multiplying the offset with direction
            # and make sure it wraps around using modulo
            new_index = (index + (offset * direction)) % len(alphabet)

            encrypted_text += alphabet[new_index]

    return encrypted_text


# Test encryption and decryption
encryption = vigenere(text, custom_key, 1)  # For encryption (direction = 1)
decryption = vigenere(encryption, custom_key, -1)  # For decryption (direction = -1)

print(f"Encrypted: {encryption}")
print(f"Decrypted: {decryption}")
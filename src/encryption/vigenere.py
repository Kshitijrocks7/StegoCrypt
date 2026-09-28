def encrypt(text, key):
    result = []
    key = ''.join(char for char in key if char.isalpha())

    if not key:
        raise ValueError("Vigenere key must contain letters.")

    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')

            encrypted_char = chr(
                (ord(char) - base + shift) % 26 + base
            )

            result.append(encrypted_char)
            key_index += 1
        else:
            result.append(char)

    return ''.join(result)


def decrypt(text, key):
    result = []
    key = ''.join(char for char in key if char.isalpha())

    if not key:
        raise ValueError("Vigenere key must contain letters.")

    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')

            decrypted_char = chr(
                (ord(char) - base - shift) % 26 + base
            )

            result.append(decrypted_char)
            key_index += 1
        else:
            result.append(char)

    return ''.join(result)

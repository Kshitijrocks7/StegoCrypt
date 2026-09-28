def create_matrix(key):
    key = ''.join(
        char.upper()
        for char in key
        if char.isalpha()
    ).replace('J', 'I')

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    sequence = ""

    for char in key + alphabet:
        if char not in sequence:
            sequence += char

    return [
        list(sequence[i:i + 5])
        for i in range(0, 25, 5)
    ]


def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col

    raise ValueError(f"Character {char} not found in Playfair matrix.")


def prepare_text(text):
    text = ''.join(
        char.upper()
        for char in text
        if char.isalpha()
    ).replace('J', 'I')

    prepared = []
    i = 0

    while i < len(text):
        first = text[i]

        if i + 1 < len(text):
            second = text[i + 1]

            if first == second:
                prepared.append(first + 'X')
                i += 1
            else:
                prepared.append(first + second)
                i += 2
        else:
            prepared.append(first + 'X')
            i += 1

    return prepared


def process_pair(pair, matrix, encrypting=True):
    first, second = pair

    row1, col1 = find_position(matrix, first)
    row2, col2 = find_position(matrix, second)

    if row1 == row2:
        shift = 1 if encrypting else -1

        return (
            matrix[row1][(col1 + shift) % 5]
            + matrix[row2][(col2 + shift) % 5]
        )

    if col1 == col2:
        shift = 1 if encrypting else -1

        return (
            matrix[(row1 + shift) % 5][col1]
            + matrix[(row2 + shift) % 5][col2]
        )

    return (
        matrix[row1][col2]
        + matrix[row2][col1]
    )


def encrypt(text, key):
    if not key.strip():
        raise ValueError("Playfair key cannot be empty.")

    matrix = create_matrix(key)
    pairs = prepare_text(text)

    return ''.join(
        process_pair(pair, matrix, True)
        for pair in pairs
    )


def decrypt(text, key):
    if not key.strip():
        raise ValueError("Playfair key cannot be empty.")

    matrix = create_matrix(key)

    text = ''.join(
        char.upper()
        for char in text
        if char.isalpha()
    ).replace('J', 'I')

    if len(text) % 2 != 0:
        text += 'X'

    pairs = [
        text[i:i + 2]
        for i in range(0, len(text), 2)
    ]

    return ''.join(
        process_pair(pair, matrix, False)
        for pair in pairs
    )

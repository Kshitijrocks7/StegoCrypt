from PIL import Image


DELIMITER = "1111111111111110"


def text_to_binary(text):
    return ''.join(
        format(byte, '08b')
        for byte in text.encode('utf-8')
    )


def binary_to_text(binary):
    data = bytearray()

    for i in range(0, len(binary), 8):
        byte = binary[i:i + 8]

        if len(byte) == 8:
            data.append(int(byte, 2))

    return data.decode('utf-8', errors='replace')


def hide_message(input_image, output_image, message):
    image = Image.open(input_image).convert("RGB")

    binary_message = text_to_binary(message)
    binary_message += DELIMITER

    width, height = image.size
    capacity = width * height * 3

    if len(binary_message) > capacity:
        raise ValueError(
            f"Message is too large for this image. "
            f"Required: {len(binary_message)} bits, "
            f"Available: {capacity} bits."
        )

    pixels = list(image.getdata())

    message_index = 0
    new_pixels = []

    for pixel in pixels:
        r, g, b = pixel

        channels = [r, g, b]

        for i in range(3):
            if message_index < len(binary_message):
                channels[i] = (
                    (channels[i] & 254)
                    | int(binary_message[message_index])
                )

                message_index += 1

        new_pixels.append(tuple(channels))

    stego_image = Image.new("RGB", image.size)
    stego_image.putdata(new_pixels)
    stego_image.save(output_image)


def extract_message(image_path):
    image = Image.open(image_path).convert("RGB")

    pixels = list(image.getdata())

    binary_data = ""

    for pixel in pixels:
        r, g, b = pixel

        binary_data += str(r & 1)
        binary_data += str(g & 1)
        binary_data += str(b & 1)

        if DELIMITER in binary_data:
            binary_message = binary_data.split(DELIMITER)[0]
            return binary_to_text(binary_message)

    raise ValueError("No hidden message was found in the image.")

from PIL import Image
from Crypto.Cipher import AES
import base64
import os
import struct

# Generate AES Key
key = os.urandom(16)  # 16-byte AES key

def pad_message(message):
    while len(message) % 16 != 0:
        message += " "  # Padding for AES block size
    return message

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

def hide_text(image_path, secret_text, output_path, key):
    img = Image.open(image_path).convert("RGB")  # Ensure RGB mode
    encrypted_message = encrypt_message(pad_message(secret_text), key)

    binary_secret = ''.join(format(ord(char), '08b') for char in encrypted_message) + '11111110'  # Stop sequence
    pixels = list(img.getdata())

    if len(binary_secret) > len(pixels) * 3:
        print("Error: Message too large for this image. Use a bigger image.")
        return

    new_pixels = []
    binary_index = 0

    for pixel in pixels:
        if isinstance(pixel, int):  # Convert grayscale to RGB
            pixel = (pixel, pixel, pixel)

        new_pixel = list(pixel)  # Convert tuple to list for modification
        
        for i in range(3):  # Modify RGB channels
            if binary_index < len(binary_secret):
                new_pixel[i] = (pixel[i] & ~1) | int(binary_secret[binary_index])
                binary_index += 1

        new_pixels.append(tuple(new_pixel))

    img.putdata(new_pixels)
    img.save(output_path)
    print("Message successfully hidden in", output_path)
    print("Save this AES Key:", key.hex())

# Default filenames
with open("message.txt", "r", encoding="utf-8") as file:
    message = file.read().strip()
hide_text("original.png", message, "stego.png", key)

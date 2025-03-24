from PIL import Image
from Crypto.Cipher import AES
import base64
import os

# AES Encryption
def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

# Hide Encrypted Message in Image
def hide_text(image_path, secret_text, output_path, key):
    img = Image.open(image_path).convert("RGB")  # Ensure image is in RGB mode
    encrypted_message = encrypt_message(secret_text, key)
    binary_secret = ''.join(format(ord(char), '08b') for char in encrypted_message) + '11111110'  # Fix stop sequence

    pixels = list(img.getdata())
    new_pixels = []

    binary_index = 0
    for pixel in pixels:
        if isinstance(pixel, int):  # If grayscale, convert to tuple
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

# Example Usage
key = os.urandom(16)  # Generate a random 16-byte AES key
hide_text("original.png", "This is a secret message!", "stego.png", key)
print("Save this AES Key:", key.hex())  # Ensure user saves the key

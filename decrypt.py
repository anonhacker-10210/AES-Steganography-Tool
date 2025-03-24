from PIL import Image
from Crypto.Cipher import AES
import base64
import binascii
import struct

def decrypt_message(encrypted_message, key):
    try:
        raw_data = base64.b64decode(encrypted_message)
        nonce, tag, ciphertext = raw_data[:16], raw_data[16:32], raw_data[32:]
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        return cipher.decrypt_and_verify(ciphertext, tag).decode('utf-8', errors='ignore')
    except Exception as e:
        return f"Decryption failed: {e}"

def extract_text(image_path, key):
    img = Image.open(image_path)
    pixels = list(img.getdata())

    binary_message = ""
    for pixel in pixels:
        for i in range(3):  # Extract from RGB channels
            binary_message += str(pixel[i] & 1)

    # Split binary into 8-bit chunks
    binary_chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]

    extracted_data = ""
    for b in binary_chars:
        if b == "11111110":  # Stop identifier
            break
        extracted_data += chr(int(b, 2))

    try:
        decrypted_message = decrypt_message(extracted_data, key)
        print("Hidden Message:", decrypted_message)
    except (ValueError, binascii.Error):
        print("Decryption failed! Incorrect key or corrupted data.")

# Default image file
key_input = input("Enter the AES Key: ")
key = bytes.fromhex(key_input)  # Convert hex key back to bytes
extract_text("stego.png", key)

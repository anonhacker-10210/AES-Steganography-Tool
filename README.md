# Image Steganography Tool

## Overview
This tool allows you to **encrypt and hide secret messages** inside PNG images using **AES encryption** and **steganography**. It also provides a way to **extract and decrypt** the hidden messages.

## Features
- **AES Encryption (EAX Mode)** for secure message protection.
- **Steganography (LSB Encoding)** to hide messages inside images.
- **Automatic File Input**: Reads the message from `message.txt`.
- **Extract & Decrypt Functionality**.
- **Easy-to-Use CLI Interface**.

## Installation
Make sure you have Python and the required libraries installed:
```bash
pip install pillow pycryptodome
```

## Usage
### 1️⃣ Hide a Message in an Image
- Place your **original image** as `original.png`.
- Write your secret message inside `message.txt`.
- Run the script:
  ```bash
  python encrypt.py
  ```
- The encrypted message will be stored inside `stego.png`.
- The script will output an **AES key**—**SAVE IT** (you need it for decryption).

### 2️⃣ Extract and Reveal the Hidden Message
- Run:
  ```bash
  python decrypt.py
  ```
- Enter the **AES Key** when prompted.
- The script will decrypt and reveal the **original hidden message**.

## File Structure
```
/ImageStegoTool
│── encrypt.py      # Script to hide messages in an image
│── decrypt.py      # Script to extract hidden messages
│── original.png    # Original image
│── stego.png       # Image with the hidden message
│── message.txt     # Text file containing the secret message
│── README.md       # Documentation
```

## Notes
- Use a **high-resolution image** for longer messages.
- If decryption fails, **ensure you enter the correct AES key**.
- The script stops reading when it finds a `11111110` binary marker.

## License
This project is open-source and free to use!


# AES Steganography Tool

## Overview

This project allows you to **encrypt** and **hide messages** inside images using **AES encryption** and **steganography**. You can also **decrypt** and **retrieve** hidden messages from images.

## Features

- **AES Encryption**: Encrypts messages before hiding them in images.
- **Steganography**: Conceals encrypted messages inside PNG images.
- **Decryption Support**: Extracts and decrypts hidden messages from stego images.
- **Secure & Simple**: Uses a user-provided AES key for encryption and decryption.

## Requirements

Make sure you have **Python 3** installed along with the following dependencies:

```bash
pip install pillow pycryptodome
```

## Usage

### 1. Hide a Message in an Image

Run the `encrypt.py` script:

```bash
python encrypt.py
```

Enter your **AES key** and the **message** you want to hide. The script will generate a `stego.png` file containing the encrypted message.

### 2. Extract and Decrypt a Message from an Image

Run the `decrypt.py` script:

```bash
python decrypt.py
```

Enter the **same AES key** you used for encryption. If the key is correct, the hidden message will be revealed.

## File Structure

```
/AES-Steganography-Tool
│── encrypt.py      # Script to encrypt and hide messages in images
│── decrypt.py      # Script to extract and decrypt messages from images
│── original.png    # Original image (before hiding message)
│── stego.png       # Image containing hidden message
│── README.md       # Project documentation
```

## Notes

- Ensure your AES key is **exactly 32 characters long**.
- Only **PNG images** are supported.
- If decryption fails, check that you're using the **correct key**.

## License

This project is **open-source** and free to use!

**Tested On Windows 10**

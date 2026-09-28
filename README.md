# StegoCrypt

### Encryption & Steganography

StegoCrypt is a Python-based security project that combines classical cryptography with **LSB (Least Significant Bit) image steganography** to provide a dual-layer approach for secure text communication.

The project allows users to encrypt text using classical encryption algorithms, hide the encrypted message inside an image, extract the hidden message, and decrypt it back to the original text.

---

## Features

- Caesar Cipher encryption and decryption
- Vigenère Cipher encryption and decryption
- Playfair Cipher encryption and decryption
- LSB image steganography
- Hide encrypted text inside images
- Extract hidden messages from images
- Decrypt extracted messages
- User-friendly interface
- Dual-layer security using encryption + steganography

---

## Workflow

```text
Original Message
       │
       ▼
Select Encryption Algorithm
       │
       ▼
Encrypt Message
       │
       ▼
Hide Encrypted Message
inside an Image using LSB
       │
       ▼
Stego Image
       │
       ▼
Extract Hidden Message
       │
       ▼
Decrypt Message
       │
       ▼
Original Message

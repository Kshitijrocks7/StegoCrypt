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


The encryption layer transforms the original message into ciphertext, while the steganography layer hides that ciphertext inside an image.

Encryption Algorithms
1. Caesar Cipher

The Caesar Cipher is a substitution cipher where each character in the plaintext is shifted by a fixed number of positions in the alphabet.

Example:

Plaintext:  HELLO
Shift:      3
Ciphertext: KHOOR

It is useful for demonstrating the basic concept of substitution-based cryptography.

2. Vigenère Cipher

The Vigenère Cipher is a polyalphabetic substitution cipher that uses a keyword to determine the character shifts applied to the plaintext.

Unlike the Caesar Cipher, the shift changes based on the characters of the key.

Example:

Plaintext: HELLO
Key:       KEY

The repeated keyword determines the encryption pattern.

3. Playfair Cipher

The Playfair Cipher encrypts text using pairs of characters rather than encrypting individual characters independently.

It uses a 5×5 key matrix generated from a keyword and applies transformation rules to each pair of plaintext characters.

This demonstrates a classical digraph substitution technique.

LSB Image Steganography

StegoCrypt uses Least Significant Bit (LSB) steganography to hide encrypted text inside an image.

Digital images contain pixel values represented using binary data. The least significant bits of these values can be modified to store information while producing minimal visible changes to the image.

Conceptually:

Original Pixel

10110110

LSB
   ↓
10110110


Modified Pixel

10110111

LSB
   ↓
10110111

The visual difference is generally very small, while the modified bits can contain hidden information.

Dual-Layer Security

The main concept behind StegoCrypt is the combination of encryption and steganography.

Instead of directly hiding plaintext inside an image:

Plaintext
   ↓
Stego Image

StegoCrypt follows:

Plaintext
   ↓
Encryption
   ↓
Ciphertext
   ↓
LSB Steganography
   ↓
Stego Image

Therefore, even if someone discovers that information is hidden inside the image, the extracted content is still encrypted.

The reverse process is:

Stego Image
   ↓
LSB Extraction
   ↓
Ciphertext
   ↓
Decryption
   ↓
Plaintext
Project Workflow
Encryption & Hiding
Enter the plaintext message.
Select an encryption algorithm.
Provide the required encryption key or parameters.
Encrypt the message.
Select a cover image.
Hide the encrypted message inside the image using LSB steganography.
Save the resulting stego image.
Extraction & Decryption
Select the stego image.
Extract the hidden ciphertext.
Select the corresponding decryption method.
Provide the required key or parameters.
Decrypt the ciphertext.
Recover the original plaintext.
Technologies Used
Python
Pillow / Python Imaging Library
Classical Cryptography
Image Processing
LSB Steganography
File Handling
GUI Development
Project Structure
StegoCrypt/
│
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── encryption/
│   │   ├── __init__.py
│   │   ├── caesar.py
│   │   ├── vigenere.py
│   │   └── playfair.py
│   │
│   └── steganography/
│       ├── __init__.py
│       └── lsb.py
│
├── tests/
│   ├── __init__.py
│   └── test_encryption.py
│
└── assets/
    └── screenshots/
Installation

Clone the repository:

git clone https://github.com/<your-username>/StegoCrypt.git

Navigate into the project directory:

cd StegoCrypt

Install the required dependencies:

pip install -r requirements.txt
Running the Project

Run the main application using:

python src/main.py

The exact command may vary depending on the final project structure and implementation.

Example Workflow
User Input
    │
    ▼
"Meet me at 6 PM"
    │
    ▼
Encryption
    │
    ▼
Encrypted Message
    │
    ▼
LSB Encoding
    │
    ▼
Image with Hidden Data
    │
    ▼
LSB Extraction
    │
    ▼
Encrypted Message
    │
    ▼
Decryption
    │
    ▼
"Meet me at 6 PM"
Security Concepts Demonstrated

This project demonstrates several important cybersecurity and information-security concepts:

Classical cryptography
Substitution ciphers
Polyalphabetic encryption
Digraph-based encryption
Image steganography
Binary data manipulation
Information hiding
Encryption and decryption
Secure communication concepts
Layered security
Limitations

The classical encryption algorithms implemented in this project are intended primarily for educational purposes and should not be considered secure alternatives to modern cryptographic algorithms.

Similarly, LSB steganography provides information hiding rather than complete cryptographic protection.

For real-world secure communication, modern authenticated encryption algorithms and secure key-management mechanisms should be used.

Future Improvements

Possible future improvements include:

AES-based encryption
Password-based key derivation
Support for additional image formats
Automatic payload-capacity detection
Message integrity verification
Authentication / MAC support
Improved GUI
Drag-and-drop image support
Secure key management
Support for larger payloads
Improved error handling and validation
Educational Purpose

StegoCrypt was developed as an educational cybersecurity project to explore the relationship between cryptography, image processing, and information hiding.

It demonstrates how multiple security techniques can be combined to create a layered approach to protecting information.

Author
Kshitij Verma
Computer Science & Engineering

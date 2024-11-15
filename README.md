# Image Encryption Tool

## Description
This is a simple image encryption tool written in Python that uses XOR encryption to encrypt and decrypt image files. The tool utilizes the `Pillow` library for image processing, `numpy` for handling pixel data as arrays, and `termcolor` for colorful terminal outputs.

The tool allows you to:
- **Encrypt** an image using a custom integer key.
- **Decrypt** an image using the same integer key.

## Features
- **Encrypt Images**: Encrypt an image using a numeric key (integer).
- **Decrypt Images**: Decrypt an encrypted image using the same numeric key.
- **Reversible Encryption**: XOR encryption ensures the process is reversible with the same key for decryption.
- **Simple Command-Line Interface**: Easy-to-use menu with options for encryption, decryption, and quitting.

## Requirements
To run this tool, you will need to install the following Python libraries:

- `Pillow`: For opening and saving image files.
- `numpy`: For handling pixel data as arrays.
- `termcolor`: For colorful terminal outputs.

You can install the required libraries by running:

```bash
pip install -r requirements.txt
```

## Installation
1. Clone or download the repository to your local machine.
2. Navigate to the directory where the script is located.
3. Create and activate a Python virtual environment (optional but recommended).

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

4. Install the required dependencies.

```bash
pip install -r requirements.txt
```

## Usage

1. **Run the script**:

```bash
python3 image_encryption_tool.py
```

2. **Select an option**:
   - **e** to encrypt an image
   - **d** to decrypt an image
   - **q** to quit the program

3. **Encrypting an image**:
   - When prompted, enter the encryption key (an integer).
   - Enter the path of the image you want to encrypt.
   - The encrypted image will be saved as `encrypted_image.png`.

4. **Decrypting an image**:
   - When prompted, enter the decryption key (the same key used for encryption).
   - Enter the path of the encrypted image.
   - The decrypted image will be saved as `decrypted_image.png`.

## Example

**Encrypting an image**:
```
Enter encryption key (integer): 1234
Enter the location or path of the image: /path/to/image.png
Image encrypted successfully. Encrypted image saved at: encrypted_image.png
```

**Decrypting an image**:
```
Enter decryption key (integer): 1234
Enter the location or path of the encrypted image: /path/to/encrypted_image.png
Image decrypted successfully. Decrypted image saved at: decrypted_image.png
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
- **G4UR4V007**

## Acknowledgments
- Thanks to [Pillow](https://python-pillow.org/) for image processing.
- Thanks to [numpy](https://numpy.org/) for efficient array manipulation.
- Thanks to [termcolor](https://pypi.org/project/termcolor/) for colorful terminal outputs.

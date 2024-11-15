from PIL import Image
import numpy as np
from termcolor import colored

def print_banner():
    print(colored("------------- Image Encryption Tool --------------", "cyan"))
    print(colored("Author: G4UR4V007", "yellow"))
    print(colored("Version: 1.0", "yellow"))
    print(colored("---------------------------------------------------", "cyan"))

def xor_encrypt_decrypt(image_array, key):
    """
    Apply XOR encryption/decryption on each pixel value.
    XOR operation is reversible, so we can use the same function for both encryption and decryption.
    """
    return np.bitwise_xor(image_array, key)

def encrypt_image(image_path, key):
    try:
        original_image = Image.open(image_path)
    except FileNotFoundError:
        print(colored("Error: Image file not found!", "red"))
        return

    image_array = np.array(original_image)
    encrypted_image_array = xor_encrypt_decrypt(image_array, key)
    encrypted_image = Image.fromarray(np.uint8(encrypted_image_array))

    encrypted_image_path = "encrypted_image.png"
    encrypted_image.save(encrypted_image_path)
    print(colored(f"Image encrypted successfully. Encrypted image saved at: {encrypted_image_path}", "green"))

def decrypt_image(encrypted_image_path, key):
    try:
        encrypted_image = Image.open(encrypted_image_path)
    except FileNotFoundError:
        print(colored("Error: Encrypted image file not found!", "red"))
        return

    encrypted_image_array = np.array(encrypted_image)
    decrypted_image_array = xor_encrypt_decrypt(encrypted_image_array, key)
    decrypted_image = Image.fromarray(np.uint8(decrypted_image_array))

    decrypted_image_path = "decrypted_image.png"
    decrypted_image.save(decrypted_image_path)
    print(colored(f"Image decrypted successfully. Decrypted image saved at: {decrypted_image_path}", "green"))

def encrypt_choice():
    try:
        key = int(input(colored("Enter encryption key (integer): ", "magenta")))
        image_location = input(colored("Enter the location or path of the image: ", "magenta"))
        encrypt_image(image_location, key)
    except ValueError:
        print(colored("Error: Invalid key. Please enter an integer.", "red"))

def decrypt_choice():
    try:
        key = int(input(colored("Enter decryption key (integer): ", "magenta")))
        encrypted_image_location = input(colored("Enter the location or path of the encrypted image: ", "magenta"))
        decrypt_image(encrypted_image_location, key)
    except ValueError:
        print(colored("Error: Invalid key. Please enter an integer.", "red"))

def main():
    print_banner()

    while True:
        print(colored("\nSelect an option:", "cyan"))
        print(colored("e - Encrypt image", "green"))
        print(colored("d - Decrypt image", "green"))
        print(colored("q - Quit", "red"))
        choice = input(colored("Your choice: ", "cyan"))

        if choice == 'e':
            encrypt_choice()
        elif choice == 'd':
            decrypt_choice()
        elif choice == 'q':
            print(colored("Exiting the program. Goodbye!", "yellow"))
            break
        else:
            print(colored("Invalid choice. Please choose 'e' for encryption, 'd' for decryption, or 'q' to quit.", "red"))

if __name__ == "__main__":
    main()

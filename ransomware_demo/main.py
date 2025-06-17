import os
from cryptography.fernet import Fernet

WARNING = """
*** WARNING ***
This is a simulated ransomware demo for educational purposes only.
It only encrypts/decrypts files in the demo_folder directory.
Do not use on important data.
"""

KEY_FILE = 'demo_folder/secret.key'
TARGET_FOLDER = 'demo_folder'


def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(key)
    return key

def load_key():
    with open(KEY_FILE, 'rb') as f:
        return f.read()

def encrypt_files(key):
    f = Fernet(key)
    for filename in os.listdir(TARGET_FOLDER):
        path = os.path.join(TARGET_FOLDER, filename)
        if os.path.isfile(path) and filename != 'secret.key':
            with open(path, 'rb') as file:
                data = file.read()
            encrypted = f.encrypt(data)
            with open(path, 'wb') as file:
                file.write(encrypted)


def decrypt_files(key):
    f = Fernet(key)
    for filename in os.listdir(TARGET_FOLDER):
        path = os.path.join(TARGET_FOLDER, filename)
        if os.path.isfile(path) and filename != 'secret.key':
            with open(path, 'rb') as file:
                data = file.read()
            try:
                decrypted = f.decrypt(data)
                with open(path, 'wb') as file:
                    file.write(decrypted)
            except Exception:
                print(f"Could not decrypt {filename} (may not be encrypted).")

def main():
    print(WARNING)
    os.makedirs(TARGET_FOLDER, exist_ok=True)
    action = input("Type 'encrypt' to lock files or 'decrypt' to unlock: ").strip().lower()
    if action == 'encrypt':
        key = generate_key()
        encrypt_files(key)
        print("Files encrypted. Key saved to demo_folder/secret.key.")
    elif action == 'decrypt':
        if not os.path.exists(KEY_FILE):
            print("No key found. Cannot decrypt.")
            return
        key = load_key()
        decrypt_files(key)
        print("Files decrypted.")
    else:
        print("Invalid action.")

if __name__ == "__main__":
    main()

from cryptography.fernet import Fernet

# set encryption key
key = b"1fKv3xGBC4cHVL_JOtFLYMeLcufNLpBGKs4nh4PxIyw="


def encrypt(message, key_size=256): # arguments: bytes or str, int
    """
    This method encrypts the inputted data and returns output as string
    """
    if type(message) == str:
        message = bytes(message, 'ascii')
    cipher = Fernet(key)
    return str(cipher.encrypt(message))[2:-1]

def decrypt(cipher_text): # argument: bytes or str
    """
    This method decrypts the encrypted text and returns output as string
    """
    if type(cipher_text) == str:
        cipher_text = bytes(cipher_text, 'ascii')
    cipher = Fernet(key)
    return str(cipher.decrypt(cipher_text))[2:-1]


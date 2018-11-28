def encrypt_caesar(plaintext):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ''
    for symbol in plaintext:
        if 'A' <= symbol <= 'Z' or 'a' <= symbol <= 'z':
            if symbol >= 'X' and symbol <= 'Z' or symbol >= 'x' and symbol <= 'z':
                ciphertext += chr(ord(symbol)+3-26)
            else:
                ciphertext += chr(ord(symbol)+3)
        else:
            ciphertext += symbol
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''
    for symbol in ciphertext:
        if 'A' <= symbol <= 'Z' or 'a' <= symbol <= 'z':
            if symbol >= 'A' and symbol <= 'C' or symbol >= 'a' and symbol <= 'c':
                plaintext += chr(ord(symbol) - 3 + 26)
            else:
                plaintext += chr(ord(symbol) - 3)
        else:
            plaintext += symbol
    return plaintext
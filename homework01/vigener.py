def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    i = 0
    ciphertext = ''
    for symbol in plaintext:
        if 'A' <= symbol <= 'Z' or 'a' <= symbol <= 'z':
            if i > len(keyword) - 1:
                i = 0
            if 'A' <= keyword[i] <= 'Z':
                symbol_1 = ord(symbol) + (ord(keyword[i]) - 65)
            elif 'a' <= keyword[i] <= 'z':
                symbol_1 = ord(symbol) + (ord(keyword[i]) - 97)
            if 'A' <= symbol <= 'Z' and symbol_1 > ord('Z') or \
                    'a' <= symbol <= 'z' and symbol_1 > ord('z'):
                symbol_1 -= 26
        i += 1
        ciphertext += chr(symbol_1)
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    i = 0
    plaintext = ''
    for symbol in ciphertext:
        if 'A' <= symbol <= 'Z' or 'a' <= symbol <= 'z':
            if i > len(keyword) - 1:
                i = 0
            if 'A' <= keyword[i] <= 'Z':
                symbol_1 = ord(symbol) - (ord(keyword[i]) - 65)
            elif 'a' <= keyword[i] <= 'z':
                symbol_1 = ord(symbol) - (ord(keyword[i]) - 97)
            if 'A' <= symbol <= 'Z' and symbol_1 < ord('A') or \
                    'a' <= symbol <= 'z' and symbol_1 < ord('a'):
                symbol_1 += 26
        i += 1
        plaintext += chr(symbol_1)
    return plaintext
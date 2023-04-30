def checkKey(message: str, key: str):
    sizeMessage = len(message)
    sizeKey = len(key)

    if (sizeKey >= sizeMessage):
        return key
    else:
        aux = sizeMessage - sizeKey
        for i in range(aux):
            key+=key[i]

        return key


def encrypt(message, key):
    sizeMessage = len(message)
    j = 0
    cipher = ""

    for i in range(sizeMessage):
        if 'a' <= message[i] <= 'z':
            letter = ((ord(message[i]) - ord('a')) + (ord(key[i-j]) - ord('a'))) % 26
            letter = chr(letter + ord('a'))
            cipher += letter
        else:
            j += 1
            cipher += message[i]

    return cipher


def decrypt(cipher: str, key: str) -> str:
    sizeCipher = len(cipher)
    j = 0
    message = ""

    for i in range(sizeCipher):
        if 'a' <= cipher[i] <= 'z':
            letter = (ord(cipher[i]) - ord(key[i-j]) + 26) % 26
            letter = chr(letter + ord('a'))
            message += letter
        else:
            j += 1
            message += cipher[i]

    return message
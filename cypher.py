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


def decrypt(cypher: str, key: str):
    sizeCypher = len(cypher)
    j =0
    message = ""
    for i in range(sizeCypher):
        if 'a' <= cypher[i] <= 'z':
            letter = (ord(cypher[i]) - key[i -j] + ord('a')) % 26
            letter = chr(letter + ord('a'))
            message += letter
        else:
            j+= 1
            message += cypher[i]
    
    return message
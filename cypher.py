##recebe uma mensagem e uma chave e retorna a chave com tamanho igual ou superior à mensagem. 
#Caso a chave seja menor que a mensagem, a função repete a chave até que ela tenha o mesmo tamanho da mensagem.
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

#recebe uma mensagem e uma chave e retorna a mensagem criptografada usando a cifra de Vigenère. 
# A função itera sobre cada letra da mensagem e da chave, desloca a letra da mensagem pelo valor correspondente na letra da chave e adiciona a letra criptografada ao resultado final.
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

#recebe uma mensagem criptografada e a chave correspondente e retorna a mensagem original descriptografada. 
# A função faz o processo inverso da função encrypt, deslocando cada letra da mensagem criptografada pela letra correspondente da chave.
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
from cypher import encrypt, decrypt, checkKey
from attack import sizeKey, attack


def menu():
    while True:
        print("***********************")
        print(" Escolha a opcao desejada:  ")
        print("1 - Criptografar")
        print("2 - Descriptografar")
        print("3 - Ataque")
        print("4 - Sair")
        option = int(input())

        if option == 1:
            message = input("Entre com o valor da mensagem\n")
            key = input("Entre com o valor da chave:\n")
            key = checkKey(message, key)
            cifra = encrypt(message, key)
            print(f'Cifra = {cifra}')
        elif option == 2:
            cypher = input("Entre com o valor da cifra:\n")
            key = input("Entre com o valor da chave:\n")
            newkey = checkKey(cypher, key)
            message = decrypt(cypher, newkey)
            print(f'Mensagem = {message}')
        elif option == 3:
            cipher = input("Entre com o valor da cifra:\n")
            print("Idiomas disponíveis:\n")
            print("1 - Inglês")
            print("2 - Português")
            language = int(input("Escolha um idioma:\n"))
            key = attack(cipher, sizeKey(cipher), language)
            key = checkKey(cipher, key)
            message = decrypt(cipher, key)
            print("\n Mensagem: " + message)
            input("\n Pressione ENTER para continuar")
        else:
            return False


menu()

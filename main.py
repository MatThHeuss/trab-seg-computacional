from cypher import encrypt, decrypt


def menu():
    print("***********************")
    print(" Escolha a opcao desejada:  ")
    print("1 - Criptografar")
    print("2 - Descriptografar")
    option = int(input())

    if option == 1:
        test = encrypt("test", "aaaa")
        print(test)
    elif option == 2:
        test =  decrypt("test", "aaaa")
        print(test)



menu()
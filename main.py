def menu():
    print("1 - Definir Armador")
    print("2 - Plantar Armadilhas")
    print("3 - Iniciar com Andarilho")
    print("4 - Mostrar o Placar")
    print("0 - Finalizar o Jogo")
    n = -1
    while n != 0:
        n = input("Digite a opção desejada: ")
        match n:
            case "0":
                print("Jogo encerrado.")
                return 1
            case _:
                print("Opção inválida.")

menu()

settings = {
    "rigger": 0,
    "wanderer": 0,
    "riggerScore": 0,
    "wandererScore": 0,
    "traps": 15
}
field = [['0', '1', '2', '3', '4', '5', '6', '7'], ['A'] * 8]


def resetField(field):
    field = [["A"] * 7] * 7


def defineRigger():
    settings["rigger"] = int(input("Qual jogador plantará as armadilhas? [1 ou 2] "))
    while (settings["rigger"] != 1) and (settings["rigger"] != 2):
        settings["rigger"] = int(input("Digite um número válido[1 ou 2]: "))
    if settings["rigger"] == 1:
        settings["wanderer"] = 2
    else:
        settings["wanderer"] = 1

    print(f'O armador é o jogador: {settings["rigger"]}')
    print(f'O andarilho é o jogador: {settings["wanderer"]}')


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

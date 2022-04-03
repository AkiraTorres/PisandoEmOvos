import os

settings = {
    "rigger": 0,
    "wanderer": 0,
    "riggerScore": 0,
    "wandererScore": 0,
    "traps": 15
}
field = []
for i in range(7):
    row = []
    for j in range(7):
        row.append("A")
    field.append(row)


def resetField(field):
    field = []
    for i in range(7):
        row = []
        for j in range(7):
            row.append("A")
        field.append(row)


def defineRigger():
    settings["rigger"] = int(input("Qual jogador plantará as armadilhas? [1 ou 2] "))
    while (settings["rigger"] != 1) and (settings["rigger"] != 2):
        settings["rigger"] = int(input("Digite um número válido[1 ou 2]: "))
    if settings["rigger"] == 1:
        settings["wanderer"] = 2
    else:
        settings["wanderer"] = 1

    print(f'O armador é o jogador: {settings["rigger"]}')
    print(f'O andarilho é o jogador: {settings["wanderer"]}\n')


def plantTraps():
    if settings["rigger"] != 1 and settings["rigger"] != 2:
        print("Armador não selecionado, por favor, defina o armador.")
        return 0

    print(f'Jogador {settings["rigger"]}, você pode esconder até 3 ovos podres por linha do terreno.')
    counter = 0
    traps = 0

    for row in field:
        for value in row:
            print(f"{value} ", end="")
        print()

    while counter < 7:
        if traps == 15:
            print(f"Você já escondeu o máximo de 15 ovos no terreno, agora é a vez do jogador {settings['wanderer']}.")
            break
        place = (int(input(f'Em qual coluna da linha {counter + 1} você quer esconder os ovos podres[1 a 7, ou 0 para passar para a próxima linha]? ')))
        if place == 0:
            print("Passando para a próxima linha.\n")
            counter+=1
            continue
        field[counter][(place - 1)] = "O"
        traps += 1
        if field[counter].count("O") == 3:
            counter+=1
            print("Você já colocou o máximo de 3 armadilhas nessa linha, vá para a próxima.\n")

    for row in field:
        for value in row:
            print(f"{value} ", end="")
        print()


def menu():
    n = -1
    while n != 0:
        print("1 - Definir Armador")
        print("2 - Plantar Armadilhas")
        print("3 - Iniciar com Andarilho")
        print("4 - Mostrar o Placar")
        print("0 - Finalizar o Jogo\n")
        n = input("Digite a opção desejada: ")
        match n:
            case "1":
                os.system("clear")
                defineRigger()
            case "2":
                plantTraps()
            case "0":
                print("Jogo encerrado.")
                return 1
            case _:
                print("Opção inválida.")


menu()

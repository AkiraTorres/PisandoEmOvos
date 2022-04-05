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


def printField() -> None:
    for row in field:
        for value in row:
            print(f"{value} ", end="")
        print()


def resetField() -> None:
    field = []
    for i in range(7):
        row = []
        for j in range(7):
            row.append("A")
        field.append(row)


def validateSpace(space: int) -> list:
    if 2 <= space and space <= 6:
        return [space - 1 ,space, space + 1]

    match space:
        case 1:
            return [1, 2]
        case 7:
            return [6, 7]
        case _:
            return [1, 2, 3, 4, 5, 6, 7]


def validateInput(validSpaces = [1, 2], str = "Qual jogador plantará as armadilhas? [1 ou 2] ") -> int:
    while True:
        space = int(input(str))

        if space in validSpaces:
            return space
        else:
            print("Entrada inválida, tente novamente.\n")


def verifyTraps(row: int, column: int) -> bool:
    if field[row][column] == "A":
        return False
    elif field[row][column] == "O":
        return True


def defineRigger() -> None:
    settings["rigger"] = validateInput()
    if settings["rigger"] == 1:
        settings["wanderer"] = 2
    else:
        settings["wanderer"] = 1

    print(f'O armador é o jogador: {settings["rigger"]}')
    print(f'O andarilho é o jogador: {settings["wanderer"]}\n')


def plantTraps() -> None:
    if settings["rigger"] != 1 and settings["rigger"] != 2:
        print("Armador não selecionado, por favor, defina o armador.")
        return 0

    print(f'Jogador {settings["rigger"]}, você pode esconder até 3 ovos podres por linha do terreno.')
    counter = 0
    traps = 0

    printField()

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

    printField()


def walk() -> None:
    for i in range(100):
        n = "=" * i
        print(n)
    
    space = 0
    for row in range(0, 7):
        validSpaces = validateSpace(space)
        print(f'Para a linha {row + 1} são válidos os espaços: {validSpaces}.')
        space = validateInput(validSpaces, 'Escolha sabiamente um dos espaços válidos: ')
        if verifyTraps(row, space - 1) == False:
            print("Ufa! Você não pisou em nenhuma armadilha dessa vez!\n")
        else:
            print("Eca! Você pisou em um ovo podre e perdeu.\n")
            settings["riggerScore"] += 1
            return -1

    print("Você atravessou o terreno sem cair em nenhuma armadilha! Parabéns!!!!")
    settings["wandererScore"] += 1


def showScoreboard() -> None:
    if settings["rigger"] == 1:
        print(f'Pontuação do Jogador 1: {settings["riggerScore"]}')
        print(f'Pontuação do Jogador 2: {settings["wandererScore"]}')
    elif settings["wanderer"] == 1:
        print(f'Pontuação do Jogador 1: {settings["wandererScore"]}')
        print(f'Pontuação do Jogador 2: {settings["riggerScore"]}')


def menu() -> None:
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
            case "3":
                walk()
            case "4":
                showScoreboard()
            case "0":
                print("Jogo encerrado.")
                return 1
            case _:
                print("Opção inválida.")


menu()

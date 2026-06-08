import random

class Mastermind:
    
    def __init__(self):
        self.__codigo = [
            random.randint(0, 9)
            for _ in range(4)
        ]

    def jugar(self):

        while True:

            intento = input(
                "Ingresa 4 números: "
            )

            if len(intento) != 4:
                print("Deben ser 4 dígitos.")
                continue

            correctos = 0

            for i in range(4):
                if int(intento[i]) == self.__codigo[i]:
                    correctos += 1

            print(
                "Correctos:",
                correctos 
            )

            if correctos == 4:
                print("Ganaste")
                break

juego = Mastermind()
juego.jugar()
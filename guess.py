import random
import json
import os


class JuegoAdivinanza:
    def __init__(self, minimo=1, maximo=100):

        self.minimo = minimo
        self.maximo = maximo

        self.numero_secreto = random.randint(
            self.minimo, self.maximo
        )

        self.intentos = 0
        self.nombre_jugador = ""

    def pedir_nombre(self):
        self.nombre_jugador = input(
            "Ingresa tu nombre: "
        )

    def pedir_numero(self):
        while True:
            try:
                numero = int(input(
                    f"Ingrese un número entre "
                    f"{self.minimo} y {self.maximo}: "
                ))

                if (
                    numero < self.minimo or
                    numero > self.maximo
                ):
                    print(
                        f"El número debe estar entre "
                        f"{self.minimo} y {self.maximo}."
                    )
                    continue

                return numero

            except ValueError:
                print(
                    "Error: Debes ingresar "
                    "un número entero válido."
                )

    def verificar_numero(self, numero):
        self.intentos += 1

        if numero < self.numero_secreto:
            print("El número secreto es MAYOR")

        elif numero > self.numero_secreto:
            print("El número secreto es MENOR")

        else:
            print("\n¡Felicidades!")
            print(
                f"Adivinaste el número "
                f"en {self.intentos} intentos"
            )

            self.guardar_resultado()

            return True

        return False

    def guardar_resultado(self):
        archivo = "resultados.json"

        nuevo_resultado = {
            "jugador": self.nombre_jugador,
            "intentos": self.intentos
        }

        # Si el archivo existe, leer datos
        if os.path.exists(archivo):
            with open(
                archivo,
                "r",
                encoding="utf-8"
            ) as file:
                try:
                    resultados = json.load(file)
                except json.JSONDecodeError:
                    resultados = []
        else:
            resultados = []

        # Agregar nuevo resultado
        resultados.append(nuevo_resultado)

        # Ordenar por menos intentos
        resultados.sort(
            key=lambda x: x["intentos"]
        )

        # Guardar nuevamente
        with open(
            archivo,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                resultados,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(
            "\nResultado guardado "
            "correctamente."
        )

        print("\n===== RANKING =====")

        for i, jugador in enumerate(
            resultados, start=1
        ):
            print(
                f"{i}. "
                f"{jugador['jugador']} - "
                f"{jugador['intentos']} intentos"
            )

    def iniciar_juego(self):
        print("====================================")
        print("     JUEGO: ADIVINA EL NÚMERO")
        print("====================================")

        print(
            f"Debes adivinar un número "
            f"entre {self.minimo} y "
            f"{self.maximo}"
        )

        self.pedir_nombre()

        while True:
            numero_usuario = self.pedir_numero()

            if self.verificar_numero(
                numero_usuario
            ):
                break


juego = JuegoAdivinanza()
juego.iniciar_juego()
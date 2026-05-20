# ============================================================
# POO en Python: Clases, Herencia, Objetos,
# Encapsulamiento, Métodos y Polimorfismo
# ============================================================

# ── CLASE BASE (Clase Padre) ─────────────────────────────────
class Animal:
    """Clase base que representa a cualquier animal."""

    # Variable de clase (compartida por todas las instancias)
    reino = "Animalia"

    def __init__(self, nombre, edad):
        # Atributos públicos
        self.nombre = nombre

        # Atributo PROTEGIDO (convención: un guion bajo)
        # Señala "uso interno", pero sigue siendo accesible
        self._edad = edad

        # Atributo PRIVADO (convención: dos guiones bajos)
        # Python lo "ofusca" → _Animal__energia
        # ENCAPSULAMIENTO: ocultamos el detalle interno
        self.__energia = 100

    # ── MÉTODOS ────────────────────────────────────────────────

    # Método getter (acceso controlado al atributo privado)
    def get_energia(self):
        return self.__energia

    # Método setter (modificación controlada)
    def set_energia(self, valor):
        if 0 <= valor <= 100:           # validación
            self.__energia = valor
        else:
            print("Energía debe estar entre 0 y 100")

    # Método de instancia común
    def respirar(self):
        print(f"{self.nombre} respira.")

    # Método que será SOBREESCRITO → base del polimorfismo
    def hablar(self):
        print("... (sonido genérico)")

    # Método de clase (recibe la clase, no la instancia)
    @classmethod
    def get_reino(cls):
        return cls.reino

    # Método estático (no depende de instancia ni clase)
    @staticmethod
    def es_vertebrado(tiene_columna):
        return tiene_columna

    # Representación legible del objeto
    def __str__(self):
        return f"Animal({self.nombre}, {self._edad} años)"


# ── HERENCIA: Perro hereda de Animal ────────────────────────
class Perro(Animal):           # ← herencia simple
    """Subclase que extiende Animal con comportamiento propio."""

    def __init__(self, nombre, edad, raza):
        # super() llama al __init__ del padre
        super().__init__(nombre, edad)
        self.raza = raza           # atributo propio de Perro

    # POLIMORFISMO: sobreescribimos hablar()
    def hablar(self):
        print(f"{self.nombre} dice: ¡Guau!")

    # Método exclusivo de Perro
    def buscar_pelota(self):
        print(f"{self.nombre} va a buscar la pelota")

    def __str__(self):
        return f"Perro({self.nombre}, raza={self.raza})"


# ── HERENCIA: Gato hereda de Animal ─────────────────────────
class Gato(Animal):
    def __init__(self, nombre, edad, es_domestico):
        super().__init__(nombre, edad)
        self.es_domestico = es_domestico

    # POLIMORFISMO: misma firma, distinto comportamiento
    def hablar(self):
        print(f"{self.nombre} dice: ¡Miau!")

    def __str__(self):
        dom = "doméstico" if self.es_domestico else "salvaje"
        return f"Gato({self.nombre}, {dom})"


# ── HERENCIA MÚLTIPLE ────────────────────────────────────────
class Mascota:
    """Mixin que añade comportamiento de mascota."""
    def jugar(self):
        print(f"{self.nombre} juega con su dueño")

class PerroMascota(Perro, Mascota):    # herencia múltiple
    """Combina Perro y Mascota."""
    pass


# ════════════════════════════════════════════════════════════
# PROGRAMA PRINCIPAL — creación de OBJETOS y pruebas
# ════════════════════════════════════════════════════════════

if __name__ == "__main__":

    # ── Crear OBJETOS (instancias) ───────────────────────────
    perro = Perro("Rex", 3, "Labrador")
    gato  = Gato("Misu", 5, True)
    pm    = PerroMascota("Buddy", 2, "Poodle")

    # ── ENCAPSULAMIENTO: acceso mediante getters/setters ─────
    print("Energía inicial:", perro.get_energia())   # 100
    perro.set_energia(80)
    print("Energía actualizada:", perro.get_energia()) # 80
    perro.set_energia(200)                             # ← rechazado

    # ── POLIMORFISMO: mismo método, distinto resultado ───────
    animales = [perro, gato, pm]
    print("\n--- Polimorfismo en acción ---")
    for a in animales:
        a.hablar()                # cada uno responde diferente
        a.respirar()              # heredado de Animal

    # ── MÉTODOS DE CLASE Y ESTÁTICOS ────────────────────────
    print("\nReino:", Animal.get_reino())
    print("¿Es vertebrado?:", Animal.es_vertebrado(True))

    # ── HERENCIA MÚLTIPLE ────────────────────────────────────
    print("\n--- Herencia múltiple ---")
    pm.hablar()
    pm.jugar()

    # ── __str__ (representación de objetos) ─────────────────
    print("\n--- Representación de objetos ---")
    for a in animales:
        print(a)

    # ── isinstance: verificar jerarquía de clases ───────────
    print("\n--- Verificación de tipos ---")
    print("¿perro es Animal?:", isinstance(perro, Animal))  # True
    print("¿gato es Perro?:",  isinstance(gato,  Perro))   # False
# camino.py
import random

# Tablero


class Tablero:
    def __init__(self, tamañox, tamañoy):
        # se crea el tablero
        self.tablero = self.crear_tablero(tamañox, tamañoy)

    def crear_tablero(self, tamañox, tamañoy):
        # Se crea lista de listas
        tablero = []
        contador = 0
        for columna in range(tamañoy):
            fila = []
            for celda in range(tamañox):
                # Se agregan los nodos
                contador += 1
                fila.append(nodo(contador, tamañox, tamañoy))
            tablero.append(fila)

        return tablero

    # Imprimir numero de la casilla
    def imprimir_tablero(self):
        for fila in self.tablero:
            for casilla in fila:
                print(casilla.numero, end=' ')
            print()

    # Imprimir coordenada X
    def imprimir_tableroX(self):
        for fila in self.tablero:
            for casilla in fila:
                print(casilla.x, end=' ')
            print()

    # Imprimir coordenada Y
    def imprimir_tableroY(self):
        for fila in self.tablero:
            for casilla in fila:
                print(casilla.y, end=' ')
            print()

# Clase nodo


class nodo:

    def __init__(self, numero, tamañox, tamañoy):
        self.numero = numero
        self.tamañox = tamañox
        self.tamañoy = tamañoy
        self.x = (numero-1) % tamañox
        self.y = (numero-1) // tamañox
        self.veces_pisado = 0

    # Saltos de un caballo
    def saltos_caballo(self):
        saltos = []
        x = self.x
        y = self.y

        if x - 2 >= 0 and y - 1 >= 0:
            saltos.append((x - 2, y - 1))

        if x - 2 >= 0 and y + 1 < self.tamañoy:
            saltos.append((x - 2, y + 1))

        if x - 1 >= 0 and y - 2 >= 0:
            saltos.append((x - 1, y - 2))

        if x - 1 >= 0 and y + 2 < self.tamañoy:
            saltos.append((x - 1, y + 2))

        if x + 1 < self.tamañox and y - 2 >= 0:
            saltos.append((x + 1, y - 2))

        if x + 1 < self.tamañox and y + 2 < self.tamañoy:
            saltos.append((x + 1, y + 2))

        if x + 2 < self.tamañox and y - 1 >= 0:
            saltos.append((x + 2, y - 1))

        if x + 2 < self.tamañox and y + 1 < self.tamañoy:
            saltos.append((x + 2, y + 1))

        return saltos

    # Saltos alfil
    def saltos_alfil(self):
        pass

    # Saltos torre
    def saltos_torre(self):
        pass

    # Saltos reina
    def saltos_reina(self):
        pass

    def saltar_caballo(self):
        saltos_posibles = self.saltos_caballo()
        cantidad_saltos = len(saltos_posibles)
        n_aleatorio = random.randint(1, cantidad_saltos)
        salto_escogido = saltos_posibles[n_aleatorio - 1]
        return salto_escogido

# Clase camino


class Camino:

    def __init__(self, tablero, casilla_inicial, cantidad_saltos):
        self.tablero = tablero
        self.T = cantidad_saltos
        self.casilla_inicial = casilla_inicial

    def simular_camino(self):
        x0 = self.casilla_inicial[0]
        y0 = self.casilla_inicial[1]
        nodo_actual = self.tablero.tablero[y0][x0]

        for i in range(self.T):
            nodo_actual.veces_pisado = nodo_actual.veces_pisado + 1
            salto = nodo_actual.saltar_caballo()
            x = salto[0]
            y = salto[1]
            nodo_actual = self.tablero.tablero[y][x]

        return nodo_actual


def probabilidad_camino(cantidad_caminos, casilla_inicial, casilla_final, cantidad_turnos):
    tablero = Tablero(8, 8)
    camino = Camino(tablero, casilla_inicial, cantidad_turnos)

    favorables = 0
    for i in range(cantidad_caminos):
        final = camino.simular_camino()
        xf = final.x
        yf = final.y

        if (xf, yf) == casilla_final:
            favorables += 1

    return favorables / cantidad_caminos


if __name__ == '__main__':
    p = probabilidad_camino(100000, (0, 0), (7, 7), 10)

    print(f"La probabilidad es : {p}")

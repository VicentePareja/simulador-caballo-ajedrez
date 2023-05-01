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
    def movimientos_caballo(self):
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
    def movimientos_alfil(self):
        movimientos = []
        x = self.x
        y = self.y

        # Movimientos en diagonal hacia arriba-izquierda
        i, j = x - 1, y - 1
        while i >= 0 and j >= 0:
            movimientos.append((i, j))
            i -= 1
            j -= 1

        # Movimientos en diagonal hacia abajo-izquierda
        i, j = x - 1, y + 1
        while i >= 0 and j < self.tamañoy:
            movimientos.append((i, j))
            i -= 1
            j += 1

        # Movimientos en diagonal hacia arriba-derecha
        i, j = x + 1, y - 1
        while i < self.tamañox and j >= 0:
            movimientos.append((i, j))
            i += 1
            j -= 1

        # Movimientos en diagonal hacia abajo-derecha
        i, j = x + 1, y + 1
        while i < self.tamañox and j < self.tamañoy:
            movimientos.append((i, j))
            i += 1
            j += 1

        return movimientos

    # Saltos torre
    def movimientos_torre(self):
        movimientos = []
        x = self.x
        y = self.y

        # Movimientos horizontales
        for i in range(self.tamañox):
            if i != x:
                movimientos.append((i, y))

        # Movimientos verticales
        for j in range(self.tamañoy):
            if j != y:
                movimientos.append((x, j))

        return movimientos

    # Saltos reina
    def movimientos_reina(self):
        movimientos = []
        x = self.x
        y = self.y

        # Movimientos horizontales
        for i in range(self.tamañox):
            if i != x:
                movimientos.append((i, y))

        # Movimientos verticales
        for j in range(self.tamañoy):
            if j != y:
                movimientos.append((x, j))

        # Movimientos en diagonal hacia arriba-izquierda
        i, j = x - 1, y - 1
        while i >= 0 and j >= 0:
            movimientos.append((i, j))
            i -= 1
            j -= 1

        # Movimientos en diagonal hacia abajo-izquierda
        i, j = x - 1, y + 1
        while i >= 0 and j < self.tamañoy:
            movimientos.append((i, j))
            i -= 1
            j += 1

        # Movimientos en diagonal hacia arriba-derecha
        i, j = x + 1, y - 1
        while i < self.tamañox and j >= 0:
            movimientos.append((i, j))
            i += 1
            j -= 1

        # Movimientos en diagonal hacia abajo-derecha
        i, j = x + 1, y + 1
        while i < self.tamañox and j < self.tamañoy:
            movimientos.append((i, j))
            i += 1
            j += 1

        return movimientos

    def movimientos_rey(self):
        movimientos = []
        x = self.x
        y = self.y

        # Las direcciones posibles del rey: arriba, abajo, izquierda, derecha y diagonales
        direcciones = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1),
        ]

        for dx, dy in direcciones:
            i, j = x + dx, y + dy
            if 0 <= i < self.tamañox and 0 <= j < self.tamañoy:
                movimientos.append((i, j))

        return movimientos

    def mover_caballo(self):
        saltos_posibles = self.movimientos_caballo()
        cantidad_saltos = len(saltos_posibles)
        n_aleatorio = random.randint(1, cantidad_saltos)
        salto_escogido = saltos_posibles[n_aleatorio - 1]
        return salto_escogido

    def mover_alfil(self):
        saltos_posibles = self.movimientos_alfil()
        cantidad_saltos = len(saltos_posibles)
        n_aleatorio = random.randint(1, cantidad_saltos)
        salto_escogido = saltos_posibles[n_aleatorio - 1]
        return salto_escogido

    def mover_torre(self):
        saltos_posibles = self.movimientos_torre()
        cantidad_saltos = len(saltos_posibles)
        n_aleatorio = random.randint(1, cantidad_saltos)
        salto_escogido = saltos_posibles[n_aleatorio - 1]
        return salto_escogido

    def mover_reina(self):
        saltos_posibles = self.movimientos_reina()
        cantidad_saltos = len(saltos_posibles)
        n_aleatorio = random.randint(1, cantidad_saltos)
        salto_escogido = saltos_posibles[n_aleatorio - 1]
        return salto_escogido

    def mover_rey(self):
        saltos_posibles = self.movimientos_rey()
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

    def simular_camino_caballo(self):
        x0 = self.casilla_inicial[0]
        y0 = self.casilla_inicial[1]
        nodo_actual = self.tablero.tablero[y0][x0]

        for i in range(self.T):
            nodo_actual.veces_pisado = nodo_actual.veces_pisado + 1
            salto = nodo_actual.mover_caballo()
            x = salto[0]
            y = salto[1]
            nodo_actual = self.tablero.tablero[y][x]

        return nodo_actual

    def simular_camino_alfil(self):
        x0 = self.casilla_inicial[0]
        y0 = self.casilla_inicial[1]
        nodo_actual = self.tablero.tablero[y0][x0]

        for i in range(self.T):
            nodo_actual.veces_pisado = nodo_actual.veces_pisado + 1
            salto = nodo_actual.mover_alfil()
            x = salto[0]
            y = salto[1]
            nodo_actual = self.tablero.tablero[y][x]

        return nodo_actual

    def simular_camino_torre(self):
        x0 = self.casilla_inicial[0]
        y0 = self.casilla_inicial[1]
        nodo_actual = self.tablero.tablero[y0][x0]

        for i in range(self.T):
            nodo_actual.veces_pisado = nodo_actual.veces_pisado + 1
            salto = nodo_actual.mover_torre()
            x = salto[0]
            y = salto[1]
            nodo_actual = self.tablero.tablero[y][x]

        return nodo_actual

    def simular_camino_reina(self):
        x0 = self.casilla_inicial[0]
        y0 = self.casilla_inicial[1]
        nodo_actual = self.tablero.tablero[y0][x0]

        for i in range(self.T):
            nodo_actual.veces_pisado = nodo_actual.veces_pisado + 1
            salto = nodo_actual.mover_reina()
            x = salto[0]
            y = salto[1]
            nodo_actual = self.tablero.tablero[y][x]

        return nodo_actual

    def simular_camino_rey(self):
        x0 = self.casilla_inicial[0]
        y0 = self.casilla_inicial[1]
        nodo_actual = self.tablero.tablero[y0][x0]

        for i in range(self.T):
            nodo_actual.veces_pisado = nodo_actual.veces_pisado + 1
            salto = nodo_actual.mover_rey()
            x = salto[0]
            y = salto[1]
            nodo_actual = self.tablero.tablero[y][x]

        return nodo_actual


def probabilidad_camino(cantidad_caminos, casilla_inicial, casilla_final, cantidad_turnos, pieza):
    tablero = Tablero(8, 8)
    camino = Camino(tablero, casilla_inicial, cantidad_turnos)

    favorables = 0

    if pieza.rstrip() == "caballo":
        for i in range(cantidad_caminos):
            final = camino.simular_camino_caballo()
            xf = final.x
            yf = final.y

            if (xf, yf) == casilla_final:
                favorables += 1

        return favorables / cantidad_caminos

    elif pieza.rstrip() == "alfil":
        for i in range(cantidad_caminos):
            final = camino.simular_camino_alfil()
            xf = final.x
            yf = final.y

            if (xf, yf) == casilla_final:
                favorables += 1

        return favorables / cantidad_caminos

    elif pieza.rstrip() == "torre":
        for i in range(cantidad_caminos):
            final = camino.simular_camino_torre()
            xf = final.x
            yf = final.y

            if (xf, yf) == casilla_final:
                favorables += 1

        return favorables / cantidad_caminos

    elif pieza.rstrip() == "reina":
        for i in range(cantidad_caminos):
            final = camino.simular_camino_reina()
            xf = final.x
            yf = final.y

            if (xf, yf) == casilla_final:
                favorables += 1

        return favorables / cantidad_caminos

    elif pieza.rstrip() == "rey":
        for i in range(cantidad_caminos):
            final = camino.simular_camino_rey()
            xf = final.x
            yf = final.y

            if (xf, yf) == casilla_final:
                favorables += 1

        return favorables / cantidad_caminos

    else:
        print("La pieza escrita no existe u ocurrió un error desconocido.")
        print("el formato de probabilidad_camino es: (n, inicial, final, pasos, pieza)")


if __name__ == '__main__':
    p = probabilidad_camino(10000, (0, 0), (7, 7), 10, "rey")

    print(f"La probabilidad es : {p}")

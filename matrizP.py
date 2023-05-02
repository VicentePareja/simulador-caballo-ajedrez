import numpy as np
from numpy.linalg import matrix_power

# Creación de la matriz de probabilidad de transición
n = 8
m = 8

# Caso caballo


def knight_transition_matrix(n, m):
    directions = [(1, 2), (2, 1), (-1, 2), (-2, 1),
                  (1, -2), (2, -1), (-1, -2), (-2, -1)]

    matrix = np.zeros((n * m, n * m))

    for i in range(n):
        for j in range(m):
            current = i * m + j
            possible_moves = 0

            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m:
                    possible_moves += 1

            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m:
                    neighbor = x * m + y
                    # No olvidar divir por la cantidad de movimientos
                    matrix[current, neighbor] = 1 / possible_moves

    return matrix

# Caso torre


def rook_transition_matrix(n, m):
    matrix = np.zeros((n * m, n * m))

    for i in range(n):
        for j in range(m):
            current = i * m + j
            # movimientos verticales y horizontales
            possible_moves = (n - 1) + (m - 1)

            for x in range(n):
                if x != i:
                    neighbor = x * m + j
                    # Se divide por la cantidad de posibilidades
                    matrix[current, neighbor] = 1 / possible_moves

            for y in range(m):
                if y != j:
                    neighbor = i * m + y
                    # Se divide por la cantidad de posibilidades
                    matrix[current, neighbor] = 1 / possible_moves

    return matrix

# Caso alfil


def bishop_transition_matrix(n, m):
    matrix = np.zeros((n * m, n * m))

    for i in range(n):
        for j in range(m):
            current = i * m + j
            possible_moves = 0

            # Contar movimientos posibles
            for x in range(n):
                for y in range(m):
                    if abs(x - i) == abs(y - j) and (x, y) != (i, j):
                        possible_moves += 1

            # Llenar la matriz con las probabilidades
            for x in range(n):
                for y in range(m):
                    if abs(x - i) == abs(y - j) and (x, y) != (i, j):
                        neighbor = x * m + y
                        matrix[current, neighbor] = 1 / possible_moves

    return matrix

# Caso reina


def queen_transition_matrix(n, m):
    queen_matrix = np.zeros((n * m, n * m))

    for i in range(n):
        for j in range(m):
            current_position = i * m + j
            possible_moves = 0

            # Contar movimientos verticales y horizontales
            for k in range(n):
                if k != i:
                    possible_moves += 1

            for l1 in range(m):
                if l1 != j:
                    possible_moves += 1

            # Contar movimientos diagonales
            for k in range(n):
                for l1 in range(m):
                    if k != i and l1 != j and abs(k - i) == abs(l1 - j):
                        possible_moves += 1

            # Llenar la matriz con las probabilidades
            for k in range(n):
                if k != i:
                    new_position = k * m + j
                    queen_matrix[current_position,
                                 new_position] = 1 / possible_moves

            for l1 in range(m):
                if l1 != j:
                    new_position = i * m + l1
                    queen_matrix[current_position,
                                 new_position] = 1 / possible_moves

            for k in range(n):
                for l1 in range(m):
                    if k != i and l1 != j and abs(k - i) == abs(l1 - j):
                        new_position = k * m + l1
                        queen_matrix[current_position,
                                     new_position] = 1 / possible_moves

    return queen_matrix

# Caso rey


def king_transition_matrix(n, m):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    matrix = np.zeros((n * m, n * m))

    for i in range(n):
        for j in range(m):
            current = i * m + j
            possible_moves = 0

            # Contar movimientos posibles
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m:
                    possible_moves += 1

            # Llenar la matriz con las probabilidades
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m:
                    neighbor = x * m + y
                    matrix[current, neighbor] = 1 / possible_moves

    return matrix

# Función para imprimir una fila (nodo de partida) de la matriz de forma visual


def print_row_as_board(row, n, m):
    row_reshaped = row.reshape((n, m))
    for i in range(n):
        for j in range(m):
            print("{:.5f} ".format(row_reshaped[i][j]), end="")
        print()
    print()


def matrix_power_n(P, n):
    return matrix_power(P, n)


if __name__ == '__main__':
    # Instancias
    knight_matrix = knight_transition_matrix(n, m)
    rook_matrix = rook_transition_matrix(n, m)
    bishop_matrix = bishop_transition_matrix(n, m)
    queen_matrix = queen_transition_matrix(n, m)
    king_matrix = king_transition_matrix(n, m)

    # Ejemplo de uso:
    # Elige la fila de la matriz que deseas imprimir (el nodo de inicio)
    nodo_inicio = 0
    num_steps = 10  # Elige el número de pasos
    # Elevar la matriz P al numero de pasos.
    P_power_n = matrix_power_n(knight_matrix, num_steps)
    # printear el tablero de probabilidades completo
    print_row_as_board(P_power_n[nodo_inicio], n, m)

import numpy as np
from numpy.linalg import matrix_power

# Creación de la matriz de probabilidad de transición
n = 8
P = np.zeros((n**2, n**2))
for i in range(n**2):
    for j in range(n**2):
        x1, y1 = i // n, i % n
        x2, y2 = j // n, j % n
        if abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
            P[i, j] = 1
        elif abs(x1 - x2) == 1 and abs(y1 - y2) == 2:
            P[i, j] = 1
    if P[i].sum() > 0:
        P[i] /= P[i].sum()

# Función para imprimir una fila de la matriz de forma visual


def print_row_as_board(row, board_size=8):
    row_reshaped = row.reshape((board_size, board_size))
    for i in range(board_size):
        for j in range(board_size):
            print("{:.2f} ".format(row_reshaped[i][j]), end="")
        print()
    print()


def matrix_power_n(P, n):
    return matrix_power(P, n)


# Ejemplo de uso:
# Elige la fila de la matriz que deseas imprimir (el nodo de inicio)
nodo_inicio = 0
num_steps = 10  # Elige el número de pasos
# Elevar la matriz P al numero de pasos.
P_power_n = matrix_power_n(P, num_steps)
# printear el tablero de probabilidades completo
print_row_as_board(P_power_n[nodo_inicio])

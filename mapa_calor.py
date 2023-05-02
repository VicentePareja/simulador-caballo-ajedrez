# mapa_calor.py
from camino import Tablero, Camino, nodo
from matrizP import (knight_transition_matrix, rook_transition_matrix,
                     bishop_transition_matrix, queen_transition_matrix, king_transition_matrix,
                     matrix_power_n)
import matplotlib.pyplot as plt
import numpy as np


def crear_tablero_a_pintar(tablero):
    tablero_a_pintar = []

    for fila in tablero.tablero:
        fila_a_pintar = []
        for celda in fila:
            num = celda.veces_pisado
            fila_a_pintar.append(num)
        tablero_a_pintar.append(fila_a_pintar)
    return tablero_a_pintar


def escalar_a_rango_01(lista_de_listas):
    # Convertir la lista de listas en un numpy array
    array_original = np.array(lista_de_listas)

    # Encontrar los valores mínimo y máximo del array
    min_val = np.min(array_original)
    max_val = np.max(array_original)

    # Escalar los valores al rango [0, 1]
    array_escalado = (array_original - min_val) / (max_val - min_val)

    return array_escalado


def crear_mapa_calor(tablero):
    fig, ax = plt.subplots()
    im = ax.imshow(tablero, cmap='coolwarm', interpolation='nearest')

    # Personalizar el gráfico
    ax.set_xticks(np.arange(tablero.shape[1]))
    ax.set_yticks(np.arange(tablero.shape[0]))
    ax.set_xticklabels(range(1, tablero.shape[1] + 1))
    ax.set_yticklabels(range(1, tablero.shape[0] + 1))

    # Añadir etiquetas para cada casilla
    """for i in range(tablero.shape[0]):
        for j in range(tablero.shape[1]):
            text = ax.text(j, i, round(tablero[i, j], 2),
                           ha="center", va="center", color="w", fontsize=8)"""

    # Mostrar el gráfico
    plt.show()


def plot_transition_heatmap(matrix, n, m, row_number=0):
    row = matrix[row_number]
    row_reshaped = row.reshape((n, m))

    plt.imshow(row_reshaped, cmap='coolwarm', interpolation='nearest')
    plt.colorbar(label='Probabilidad de transición')
    plt.title(f'Heatmap del promedio de la fila 0 y 1 de la matriz de transición')
    plt.show()


def main(inicial, n):
    tablero = Tablero(8, 8)
    camino = Camino(tablero, inicial, n)
    camino.simular_camino_caballo()
    tablero_a_pintar = crear_tablero_a_pintar(tablero)
    array_escalado = escalar_a_rango_01(tablero_a_pintar)
    crear_mapa_calor(array_escalado)


def main2(inicial, size, repeticiones):
    n, m = size
    t = repeticiones
    Pmatrix = knight_transition_matrix(n, m)
    Pmatrix_n = matrix_power_n(Pmatrix, t)
    Pmatrix_n[0] = (Pmatrix_n[0] + Pmatrix_n[1])/2
    row_number = inicial

    plot_transition_heatmap(Pmatrix_n, n, m, row_number)


if __name__ == '__main__':

    # Ver mapa de calor de simulación de camino. editar main para ver otras piezas.
    main((0, 0), 1000000)

    # Ver mapa de calor teórico. editar main2 para ver otras piezas.
    # main2(0, (8, 8), 100000)

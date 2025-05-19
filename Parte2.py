import time
import matplotlib.pyplot as plt
import seaborn as sns
import math
import numpy as np


# Parametros para el generador
# Sacados del generador de Microsoft Visual C++
a = 1664525
c = 1013904223
m = 2**32


def semilla():
    return time.time_ns() % m


def lcg(semilla, n):
    numeros = []
    x = semilla
    for _ in range(n):
        x = (a * x + c) % m
        numeros.append(x / m)
    return numeros


def graficar_histograma(muestra):
    plt.figure(figsize=(8, 5))
    sns.histplot(muestra, kde=True, bins=10, color='skyblue', edgecolor='black')
    plt.title("Muestra de 100 variables uniformes en [0,1]")
    plt.xlabel("Valor")
    plt.ylabel("Frecuencia")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# SEGUNDA PARTE
def transformar_cauchy(variables_uniformes):
    # Transforma una lista de variables U[0,1] a variables con distribución Cauchy estándar
    return [math.tan(math.pi * (u - 0.5)) for u in variables_uniformes]


def densidad_cauchy(x):
    return 1 / (math.pi * (1 + x**2))


def graficar_cauchy(muestra):
    plt.figure(figsize=(8, 5))

    # Histograma + KDE
    sns.histplot(muestra, kde=True, stat="density", bins=50, color='lightcoral', edgecolor='black',
                 label="Estimación KDE")

    # Densidad teórica de la Cauchy
    x_vals = np.linspace(-10, 10, 1000)
    y_vals = [densidad_cauchy(x) for x in x_vals]
    plt.plot(x_vals, y_vals, label='Densidad teórica', color='blue')

    plt.title("Muestra de 100 variables Cauchy estándar")
    plt.xlabel("Valor")
    plt.ylabel("Densidad")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    seed = semilla()
    
    muestra_uniforme = lcg(seed, 100)
    muestra_cauchy = transformar_cauchy(muestra_uniforme)

    graficar_histograma(muestra_uniforme)
    graficar_cauchy(muestra_cauchy)


if __name__ == '__main__':
    main()

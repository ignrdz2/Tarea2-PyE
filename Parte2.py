import time
import matplotlib.pyplot as plt
import seaborn as sns


# Parametros para el generador
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


def main():
    seed = semilla()
    muestra = lcg(seed, 100)
    print(muestra)
    graficar_histograma(muestra)


if __name__ == '__main__':
    main()

import pandas as pd
import matplotlib.pyplot as plt
import math

def leer_datos_csv(nombre_archivo):
    datos = pd.read_csv(nombre_archivo)
    return datos['cancelaciones'].tolist()

def tabla_frecuencias(cancelaciones):
    #Calcula e imprime la tabla de frecuencias absolutas, probabilidades empíricas y distribución acumulada de las cancelaciones.
    print("1. Tabla de frecuencias")
    conteo = {}
    for valor in cancelaciones:
        if valor in conteo:
            conteo[valor] += 1
        else:
            conteo[valor] = 1
    valores_ordenados = sorted(conteo.keys())
    n = len(cancelaciones)
    print("Cancelaciones | Freq.Abs | Prob.Empirica | Dist.Acumulada")
    acumulada = 0
    for valor in valores_ordenados:
        freq_abs = conteo[valor]
        prob_emp = freq_abs / n
        acumulada += prob_emp
        print(f"{valor:11d} | {freq_abs:8d} | {prob_emp:12.4f} | {acumulada:12.4f}")
    print()
    return conteo, valores_ordenados, n

def esperanza_varianza(cancelaciones, n):
    #Calcula e imprime la esperanza (media) y varianza empírica de las cancelaciones.
    print("2. Esperanza y varianza empiricas")
    suma = sum(cancelaciones)
    esperanza = suma / n
    print(f"Esperanza: {esperanza:.4f} cancelaciones por dia")
    suma_cuadrados = sum((x - esperanza)**2 for x in cancelaciones)
    varianza = suma_cuadrados / (n - 1)
    print(f"Varianza: {varianza:.4f}")
    print()
    return esperanza, varianza

def calcular_cuartil(datos_ord, q):
    #Calcula el cuartil q-ésimo usando interpolación lineal si es necesario.

    pos = (len(datos_ord) - 1) * q
    if pos == int(pos):
        return datos_ord[int(pos)]
    else:
        lower = datos_ord[int(pos)]
        upper = datos_ord[int(pos) + 1]
        return lower + (pos - int(pos)) * (upper - lower)

def mediana_rango_intercuartilico(cancelaciones):
    #Calcula e imprime la mediana y rango intercuartílico (IQR),
    #y muestra un diagrama de cajas de las cancelaciones.
    
    print("3. Mediana y rango intercuartilico")
    datos_ordenados = sorted(cancelaciones)
    q1 = calcular_cuartil(datos_ordenados, 0.25)
    mediana = calcular_cuartil(datos_ordenados, 0.5)
    q3 = calcular_cuartil(datos_ordenados, 0.75)
    iqr = q3 - q1
    print(f"Minimo: {min(cancelaciones)}")
    print(f"Q1: {q1:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Q3: {q3:.2f}")
    print(f"Maximo: {max(cancelaciones)}")
    print(f"Rango intercuartilico (IQR): {iqr:.2f}")
    print()
    plt.figure(figsize=(10, 6))
    plt.boxplot(cancelaciones, patch_artist=True,
               boxprops=dict(facecolor='skyblue', alpha=0.7),
               medianprops=dict(color='red', linewidth=2))
    plt.title('Diagrama de Cajas - Cancelaciones Diarias')
    plt.ylabel('Numero de Cancelaciones')
    plt.grid(True, alpha=0.3)
    plt.show()

def histograma_cancelaciones(cancelaciones):
    print("4. Histograma")
    plt.figure(figsize=(12, 7))
    plt.hist(cancelaciones, bins=range(min(cancelaciones), max(cancelaciones)+2),
             alpha=0.7, color='skyblue', edgecolor='black')
    plt.title('Histograma de Cancelaciones Diarias')
    plt.xlabel('Numero de Cancelaciones')
    plt.ylabel('Frecuencia')
    plt.grid(True, alpha=0.3)
    plt.show()
    print()

def ajuste_poisson(cancelaciones, conteo, valores_ordenados, n, esperanza, varianza):
    #Genera y muestra un histograma de las cancelaciones diarias.
    print("5. Comparacion con distribucion de Poisson")
    lambda_poisson = esperanza
    print(f"Parametro λ estimado: {lambda_poisson:.4f}")
    prob_teoricas = {}
    for k in valores_ordenados:
        prob_teoricas[k] = (lambda_poisson**k * math.exp(-lambda_poisson)) / math.factorial(k)
    print("\nComparación de probabilidades:")
    print("Valor | Prob.Empirica | Prob.Poisson | Diferencia")
    for valor in valores_ordenados:
        prob_emp = conteo[valor] / n
        prob_pois = prob_teoricas[valor]
        diff = abs(prob_emp - prob_pois)
        print(f"{valor:5d} | {prob_emp:12.4f} | {prob_pois:11.4f} | {diff:9.4f}")
    plt.figure(figsize=(14, 8))
    plt.hist(cancelaciones, bins=range(min(cancelaciones), max(cancelaciones)+2),
             alpha=0.6, density=True, color='skyblue', edgecolor='black',
             label='Datos empiricos')
    x_vals = list(range(min(cancelaciones), max(cancelaciones)+1))
    y_vals = [prob_teoricas[x] for x in x_vals]
    plt.plot(x_vals, y_vals, 'ro-', markersize=6, linewidth=2,
             label=f'Poisson(λ={lambda_poisson:.3f})')
    plt.title('Comparacion: Datos Empiricos vs Distribucion de Poisson')
    plt.xlabel('Numero de Cancelaciones')
    plt.ylabel('Probabilidad')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
    print("¿Es razonable el modelo de Poisson?")
    print("Si, parece razonable porque:")
    print("- Los datos son conteos de eventos en intervalos fijos")
    print(f"- La media ({esperanza:.3f}) y varianza ({varianza:.3f}) son parecidos")
    print("- El patron del histograma se parece a una Poisson")
    print()
    return lambda_poisson

def probabilidades_poisson(lambda_poisson):
    #Calcula e imprime probabilidades específicas usando la distribución de Poisson.
    print("6. Probabilidades especificas usando Poisson")
    prob_menor_5 = 0
    for k in range(0, 5):
        prob_k = (lambda_poisson**k * math.exp(-lambda_poisson)) / math.factorial(k)
        prob_menor_5 += prob_k
    print(f"P(X < 5) = {prob_menor_5:.4f}")
    print(f"Probabilidad de que haya menos de 5 cancelaciones en un día: {prob_menor_5:.4f}")
    prob_menor_igual_15 = 0
    for k in range(0, 16):
        prob_k = (lambda_poisson**k * math.exp(-lambda_poisson)) / math.factorial(k)
        prob_menor_igual_15 += prob_k
    prob_mayor_15 = 1 - prob_menor_igual_15
    print(f"P(X > 15) = {prob_mayor_15:.4f}")
    print(f"Probabilidad de que haya mas de 15 cancelaciones en un dia: {prob_mayor_15:.4f}")

def main():
    cancelaciones = leer_datos_csv('cancelaciones.csv')
    print("Parte 1: Problema de cancelación de cuentas en una aplicación Web")
    print(f"Total de días analizados: {len(cancelaciones)}\n")
    # 1. Tabla de frecuencias
    conteo, valores_ordenados, n = tabla_frecuencias(cancelaciones)
    # 2. Esperanza y varianza
    esperanza, varianza = esperanza_varianza(cancelaciones, n)
    # 3. Mediana y rango intercuartílico con boxplot
    mediana_rango_intercuartilico(cancelaciones)
    # 4. Histograma de cancelaciones
    histograma_cancelaciones(cancelaciones)
    # 5. Ajuste a Poisson y comparación
    lambda_poisson = ajuste_poisson(cancelaciones, conteo, valores_ordenados, n, esperanza, varianza)
    # 6. Probabilidades específicas de Poisson
    probabilidades_poisson(lambda_poisson)

if __name__ == '__main__':
    main()
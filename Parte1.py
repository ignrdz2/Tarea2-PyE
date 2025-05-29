import pandas as pd
import matplotlib.pyplot as plt
import math

datos = pd.read_csv('cancelaciones.csv')
cancelaciones = datos['cancelaciones'].tolist()

print(" Parte 1: Problema de cancelacion de cuentas en una aplicacion Web")
print(f"Total de dias analizados: {len(cancelaciones)}")
print()

# 1. Tabla de frecuencias absolutas, probabilidades empiricas y distribucion acumulada

print("1. Tabla de frecuencias")

# Contar cuantas veces aparece cada valor
conteo = {}
for valor in cancelaciones:
    if valor in conteo:
        conteo[valor] += 1
    else:
        conteo[valor] = 1

# Ordenar los valores
valores_ordenados = sorted(conteo.keys())
n = len(cancelaciones)

# Crear la tabla
print("Cancelaciones | Freq.Abs | Prob.Empirica | Dist.Acumulada")

acumulada = 0
for valor in valores_ordenados:
    freq_abs = conteo[valor]
    prob_emp = freq_abs / n
    acumulada += prob_emp
    print(f"{valor:11d} | {freq_abs:8d} | {prob_emp:12.4f} | {acumulada:12.4f}")

print()

# 2. Esperanza y varianza empiricas

print("2. Esperanza y varianza empiricas")

# Calcular la esperanza
suma = sum(cancelaciones)
esperanza = suma / n
print(f"Esperanza: {esperanza:.4f} cancelaciones por dia")

# Calcular la varianza
suma_cuadrados = sum((x - esperanza)**2 for x in cancelaciones)
varianza = suma_cuadrados / (n - 1)  

print(f"Varianza: {varianza:.4f}")
print()

# 3. Mediana y rango intercuartilico + diagrama de cajas

print("3. Mediana y rango intercuartilico")

# Ordenar los datos
datos_ordenados = sorted(cancelaciones)

# Calcular cuartiles
def calcular_cuartil(datos_ord, q):
    pos = (len(datos_ord) - 1) * q
    if pos == int(pos):
        return datos_ord[int(pos)]
    else:
        lower = datos_ord[int(pos)]
        upper = datos_ord[int(pos) + 1]
        return lower + (pos - int(pos)) * (upper - lower)

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

# Crear diagrama de cajas
plt.figure(figsize=(10, 6))
plt.boxplot(cancelaciones, patch_artist=True, 
           boxprops=dict(facecolor='skyblue', alpha=0.7),
           medianprops=dict(color='red', linewidth=2))
plt.title('Diagrama de Cajas - Cancelaciones Diarias')
plt.ylabel('Numero de Cancelaciones')
plt.grid(True, alpha=0.3)
plt.show()

# 4. Histograma de cancelaciones diarias

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

# 5. Ajuste a distribución de Poisson

print("5. Comparacion con distribucion de Poisson")

# Para Poisson, usamos la media como parámetro lambda
lambda_poisson = esperanza
print(f"Parametro λ estimado: {lambda_poisson:.4f}")

# Calcular probabilidades teóricas de Poisson para cada valor
prob_teoricas = {}
for k in valores_ordenados:
    # P(X = k) = (λ^k * e^(-λ)) / k!
    prob_teoricas[k] = (lambda_poisson**k * math.exp(-lambda_poisson)) / math.factorial(k)

# Comparar con las probabilidades empíricas
print("\nComparación de probabilidades:")
print("Valor | Prob.Empirica | Prob.Poisson | Diferencia")
for valor in valores_ordenados:
    prob_emp = conteo[valor] / n
    prob_pois = prob_teoricas[valor]
    diff = abs(prob_emp - prob_pois)
    print(f"{valor:5d} | {prob_emp:12.4f} | {prob_pois:11.4f} | {diff:9.4f}")

# Crear histograma superpuesto
plt.figure(figsize=(14, 8))

# Histograma empírico (en densidad)
plt.hist(cancelaciones, bins=range(min(cancelaciones), max(cancelaciones)+2), 
         alpha=0.6, density=True, color='skyblue', edgecolor='black', 
         label='Datos empiricos')

# Distribución de Poisson
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

# 6. Probabilidades especificas con modelo Poisson

print("6. Probabilidades especificas usando Poisson")

# P(X < 5) = P(X = 0) + P(X = 1) + P(X = 2) + P(X = 3) + P(X = 4)
prob_menor_5 = 0
for k in range(0, 5):
    prob_k = (lambda_poisson**k * math.exp(-lambda_poisson)) / math.factorial(k)
    prob_menor_5 += prob_k

print(f"P(X < 5) = {prob_menor_5:.4f}")
print(f"Probabilidad de que haya menos de 5 cancelaciones en un día: {prob_menor_5:.4f}")

# P(X > 15) = 1 - P(X ≤ 15)
prob_menor_igual_15 = 0
for k in range(0, 16):
    prob_k = (lambda_poisson**k * math.exp(-lambda_poisson)) / math.factorial(k)
    prob_menor_igual_15 += prob_k

prob_mayor_15 = 1 - prob_menor_igual_15
print(f"P(X > 15) = {prob_mayor_15:.4f}")
print(f"Probabilidad de que haya mas de 15 cancelaciones en un dia: {prob_mayor_15:.4f}")

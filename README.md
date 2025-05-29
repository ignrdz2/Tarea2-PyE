# Tarea 2 - Probabilidad y Estadística Aplicada

Este repositorio contiene el desarrollo completo de la Tarea 2 de la materia **Probabilidad y Estadística Aplicada**, realizada por el Equipo 3 (UCU, 2025).

## Contenido
La tarea se divide en dos partes que abordan distintos enfoques del análisis de datos y simulación de variables aleatorias en Python:

### 1. Cancelación de cuentas en una aplicación web
- **Script**: `Parte1.py`
- **Descripción**: Se analiza la cantidad diaria de cancelaciones de cuentas en una aplicación durante un período de 6 meses a partir de un archivo `.csv` proporcionado.
- **Aspectos cubiertos**:
  - Tabla con frecuencias absolutas, probabilidades empíricas y distribución acumulada.
  - Cálculo de esperanza y varianza empíricas.
  - Mediana y rango intercuartílico; diagrama de cajas.
  - Histograma de cancelaciones diarias.
  - Ajuste de una distribución de Poisson:
    - Comparación gráfica con función de masa de probabilidad.
    - Cálculo de probabilidades para eventos extremos (menos de 5 cancelaciones y más de 15).

### 2. Simulación de variables aleatorias continuas
- **Script**: `Parte2.py`
- **Descripción**: Se implementan algoritmos para la simulación de distribuciones continuas usando generadores pseudoaleatorios.
- **Aspectos cubiertos**:
  - Generación de variables uniformes continuas en [0, 1] con el algoritmo LCG (Linear Congruential Generator).
  - Creación de una muestra de tamaño 100 de variables independientes uniformes.
  - Estimación de densidad por núcleos y gráfico con curva suavizada.
  - Demostración del método de la inversa para transformar una variable uniforme en otra distribución.
  - Simulación de la distribución **Cauchy estándar** mediante el método de la inversa:
    - Generación de muestra de tamaño 100.
    - Histograma y curva de densidad estimada vs. densidad teórica.

## Cómo usar

Clonar el repositorio y ejecutar cada archivo de manera individual desde un compilador o la terminal. Es importante asegurarse de tener todas las librerias necesarias instaladas (para eso es el primer comando).

```bash
pip install numpy matplotlib seaborn pandas scipy // Necesario solo la primera vez
python Parte1.py // Ejecutar parte 1
python Parte2.py // Ejecutar parte 2

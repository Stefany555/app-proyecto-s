import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.header("📈 Cortes con los Ejes")

# Explicación general
st.markdown(r"""
En una **función racional**, los cortes con los ejes son los puntos donde la función intersecta los ejes 
\($x$\) y \($y$\).

### Corte con el eje \(x\):
El corte con el eje \($x$\) ocurre cuando \($y = 0$\). Es decir, se debe resolver la ecuación:
$$ N(x) = 0 $$

### Corte con el eje \(y\):
El corte con el eje \($y$\) ocurre cuando \($x = 0$\). Se debe calcular el valor de \($f(0)$\), que es:
$$ f(0) = \frac{N(0)}{D(0)} $$

Donde \($N(x)$\) es el numerador y \($D(x)$\) es el denominador de la función racional.
""")

# Ejemplo práctico
st.subheader("📊Ejemplo: Hallar los cortes con los ejes de la función:")
st.latex(r"""
f(x) = \frac{x^2 - 1}{x^2 - 4}
""")
st.markdown(r"""
1. **Corte con el eje \($x$\)**:
   Resolvemos \($x^2 - 1 = 0$\), es decir, \($x = \pm 1$\).
   
2. **Corte con el eje \($y$\)**:
   Calculamos \($f(0) = \frac{0^2 - 1}{0^2 - 4} = \frac{-1}{-4} = \frac{1}{4}$\).
   
Por lo tanto, los cortes con los ejes son: \($x = 1, -1$\) y \($y = \frac{1}{4}$\).
""")

# Interacción con el usuario
st.subheader("📊¡Ahora te toca a ti!")


st.subheader("🧮Analiza la función")
st.latex(r"f(x) = \frac{2x^2 - 3}{x^2 - 1}")

# **Corte con el eje y**: Este es el valor de la función en \(x = 0\)
corte_y = (2 * 0**2 - 3) / (0**2 - 1)  # Evaluar en x = 0

# **Corte con el eje x**: Son las raíces de la función, es decir, los valores de x cuando f(x) = 0
# Resolviendo 2x^2 - 3 = 0 -> x^2 = 3/2 -> x = ± sqrt(3/2)
corte_x = np.roots([2, 0, -3])  # Resuelve la ecuación 2x^2 - 3 = 0

# Mostrar información sobre los cortes
st.write(r"""
1. **Corte con el eje y**: Es el valor de la función cuando \($x = 0$\).
2. **Corte con el eje x**: Son las raíces de la ecuación \($f(x) = 0$\), es decir, donde el numerador es igual a cero.
""")

# Opción para que el usuario elija el corte con el eje y
st.write("### ¿Cuál es el valor de la función en \($x = 0$\)? (Corte con el eje \($y$\))")
opcion_corte_y = st.radio("Selecciona la opción correcta", 
    (f"f(0) = {corte_y}", 
     f"f(0) = 2", 
     f"f(0) = -2", 
     f"f(0) = 0"))

# Mostrar la respuesta sobre el corte con el eje y
if opcion_corte_y == f"f(0) = {corte_y}":
    st.success("¡Correcto! El valor de la función en \(x = 0\) es \( f(0) = -3 \).")
else:
    st.error(f"Incorrecto. El valor correcto es \( f(0) = {corte_y} \).")

# Opción para que el usuario elija los cortes con el eje x
st.write(r"### ¿Cuáles son los valores de \($x$\) cuando \($f(x) = 0$\)? (Cortes con el eje \($x$\))")
opcion_corte_x = st.radio("Selecciona los cortes con el eje \(x\)", 
    (f"x = {corte_x[0]} y x = {corte_x[1]}", 
     "x = 1 y x = -1", 
     "x = 0", 
     "x = 2 y x = -2"))

# Mostrar la respuesta sobre los cortes con el eje x
if opcion_corte_x == f"x = {corte_x[0]} y x = {corte_x[1]}":
    st.success(f"¡Correcto! Los cortes con el eje \(x\) son \(x = {corte_x[0]:.2f}\) y \(x = {corte_x[1]:.2f}\).")
else:
    st.error(f"Incorrecto. Los cortes correctos son \(x = {corte_x[0]:.2f}\) y \(x = {corte_x[1]:.2f}\).")

# Función para graficar la función
x = np.linspace(-3, 3, 400)
y = (2 * x**2 - 3) / (x**2 - 1)

fig, ax = plt.subplots()
ax.plot(x, y, label=r"$f(x) = \frac{2x^2 - 3}{x^2 - 1}$")
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)
ax.scatter([0], [corte_y], color='red', zorder=5)  # Marca el corte con el eje y
ax.scatter(corte_x, [0, 0], color='blue', zorder=5)  # Marca los cortes con el eje x
ax.set_ylim(-10, 10)  # Limitar los valores de y para una mejor visualización
ax.set_xlim(-3, 3)  # Limitar los valores de x
ax.legend()

# Mostrar la gráfica
st.pyplot(fig)



















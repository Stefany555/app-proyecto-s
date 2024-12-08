import streamlit as st
import random 

# Título de la sección
st.title("Dominio y rango de Funciones Racionales")

# Subtítulo
st.header("📊Domino de una funcion racional")

# Explicación general
st.markdown(r"""
El **dominio** de una función es el conjunto de todos los valores que la variable independiente (generalmente \($x$\)) 
puede tomar para los cuales la función está definida.

En el caso de las **funciones racionales**, estas están definidas como el cociente de dos polinomios:
""")

# Fórmula
st.latex(r"f(x) = \frac{P(x)}{Q(x)}")

st.markdown(r"""
Para que una función racional esté bien definida, su denominador \( $Q(x)$ \) no debe ser igual a cero, ya que 
la división entre cero no está definida. Por lo tanto, el dominio se determina excluyendo los valores de \( $x$ \) 
que anulan \( $Q(x)$ \).
""")

# Subtítulo
st.header("¿Cómo hallar el dominio de una función racional?")

# Pasos
st.markdown(r"""
Sigue estos pasos para determinar el dominio de una función racional:
1. Identifica el denominador de la función, \( $Q(x)$ \).
2. Encuentra los valores de \( $x$ \) que hacen que \( $Q(x)$ = 0 \).
3. Excluye estos valores del dominio.
4. El dominio será todos los números reales menos los valores que anulan el denominador.
""")

# Ejemplo práctico
st.subheader("Ejemplo")
st.markdown("""
Consideremos la función racional:
""")
st.latex(r"f(x) = \frac{x^2 + 3}{x - 1}")

st.markdown(r"""
1. El denominador es \( $Q(x) = x - 1$ \).
2. Resolvemos \( $Q(x) = 0$ \): \( $x - 1 = 0$ \), lo que da \( $x = 1$ \).
3. Por lo tanto, el dominio es todos los números reales excepto \( $x = 1$ \).

Resultado:
""")
st.latex(r"x \in \mathbb{R} \setminus \{1\}")


import streamlit as st
import sympy as sp

# Título y encabezado
st.header("📊 Rango de una función racional")

# Introducción al tema
st.markdown("""
El **rango** de una función es el conjunto de valores que puede tomar la función en el eje \(y\). 
Para las funciones racionales, estos valores dependen del comportamiento de la función en su dominio.

Una función racional tiene la forma general:
""")
st.latex(r"f(x) = \frac{P(x)}{Q(x)}")
st.markdown(r"""
donde:
- \($P(x)$\): Numerador (polinomio).  
- \($Q(x)$\): Denominador (polinomio).  
""")

# Pasos para calcular el rango
st.subheader("🧮 ¿Cómo se calcula el rango?")
st.markdown(r"""
1. Identifica los valores que hacen que el denominador sea cero (\($Q(x) = 0$\)).  
2. Encuentra las asíntotas horizontales o inclinadas analizando el comportamiento de la función para:
""")
st.latex(r"x \to \infty \quad \text{y} \quad x \to -\infty")
st.markdown(r"""
3. Resuelve \($f(x) = y$\) para verificar qué valores de \($y$\) no son posibles.  
4. Revisa si hay restricciones adicionales.  
""")


# Ejemplo práctico
st.subheader("📘 Ejemplo práctico")
st.markdown("Encuentra el rango de la función:")
st.latex(r"f(x) = \frac{x+1}{x-2}")
st.markdown(r"""
1. **Dominio**: El denominador es cero cuando:
""")
st.latex(r"x = 2 \quad \text{por lo que} \quad x \neq 2")
st.markdown("""
2. **Asíntota horizontal**: Analizando el comportamiento para:
""")
st.latex(r"x \to \infty \quad \text{y} \quad x \to -\infty")
st.markdown("""
La función tiende a:
""")
st.latex(r"f(x) \to 1")
st.markdown("""
Esto implica que la función no toma el valor:
""")
st.latex(r"y = 1")


st.markdown("""
3. **Resolviendo la ecuación**:
""")
st.latex(r"y = \frac{x+1}{x-2}")
st.markdown("""
Pasos:
""")
st.markdown(r"""
- Multiplicamos ambos lados por \($x - 2$\):
""")
st.latex(r"y(x-2) = x+1")
st.markdown(r"""
- Reorganizamos para despejar \($x$\):
""")
st.latex(r"x(y-1) = 2y+1")
st.markdown("""
- Finalmente, expresamos \(x\) en función de \(y\):
""")
st.latex(r"x = \frac{2y+1}{y-1}")
st.markdown(r"""
Concluimos que el rango incluye todos los valores reales excepto \($y = 1$\), que no es alcanzable debido a una restricción en el denominador.
""")

st.markdown("""
**Resultado:** 
""")
st.latex(r"y \in \mathbb{R}, \, y \neq 1")


import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
st.subheader("Hora de practicar")

# Definimos una nueva función racional
st.markdown("**Función Racional a Analizar**")
x = sp.Symbol('x')
func = (x**2 - 4) / (x**2 - 1)  # Nueva función: (x^2 - 4) / (x^2 - 1)
st.latex(f"f(x) = {sp.latex(func)}")

# Mostrar gráfica de la función (más pequeña)
st.markdown("### Gráfica de la Función")
x_vals = np.linspace(-5, 5, 500)
y_vals = [(float(func.subs(x, val)) if val != 1 and val != -1 else None) for val in x_vals]

# Reducción del tamaño de la gráfica
plt.figure(figsize=(5, 3))  # Ajustamos aún más el tamaño de la gráfica
plt.plot(x_vals, y_vals, label=r"$f(x) = \frac{x^2 - 4}{x^2 - 1}$", color="blue")
plt.axvline(x=1, color="red", linestyle="--", label="Asíntota vertical ($x = 1$)")
plt.axvline(x=-1, color="red", linestyle="--", label="Asíntota vertical ($x = -1$)")
plt.axhline(y=0, color="green", linestyle="--", label="Asíntota horizontal ($y = 0$)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gráfica de la Función Racional")
plt.grid(True)
plt.legend()
st.pyplot(plt)

# Interacción: Selección del Dominio
st.markdown("### Pregunta 1: ¿Cuál es el dominio de la función?")
opciones_dominio = [
    r"$x \in \mathbb{R}, x \neq 1, -1$", 
    r"$x \in \mathbb{R}, x > 1$", 
    r"$x \in \mathbb{R}, x < -1$"
]
respuesta_dominio = st.radio("Selecciona el dominio correcto:", opciones_dominio)

# Interacción: Selección del Rango
st.markdown("### Pregunta 2: ¿Cuál es el rango de la función?")
opciones_rango = [
    r"$y \in \mathbb{R}, y \neq 0$", 
    r"$y \in \mathbb{R}, y > 0$", 
    r"$y \in \mathbb{R}, y < 0$"
]
respuesta_rango = st.radio("Selecciona el rango correcto:", opciones_rango)

# Botón de verificación de respuestas
if st.button("Verificar Respuesta"):
    # Verificar la respuesta del dominio
    if respuesta_dominio == r"$x \in \mathbb{R}, x \neq 1, -1$":
        st.success("¡Correcto! El denominador es cero cuando $x = 1$ y $x = -1$, por lo que $x \neq 1$ y $x \neq -1$.")
    else:
        st.error("Respuesta incorrecta. El denominador se anula en $x = 1$ y $x = -1$, por lo que deben ser excluidos del dominio.")
        st.markdown("### Solución del Dominio:")
        st.markdown("El dominio de la función es todo $\\mathbb{R}$ excepto $x = 1$ y $x = -1$.")
        st.latex(r"x \in \mathbb{R}, x \neq 1, -1")

    # Verificar la respuesta del rango
    if respuesta_rango == r"$y \in \mathbb{R}, y \neq 0$":
        st.success("¡Correcto! La función tiene una asíntota horizontal en $y = 0$, por lo que $y \neq 0$.")
    else:
        st.error("Respuesta incorrecta. La función tiene una asíntota horizontal en $y = 0$ y nunca alcanza este valor.")
        st.markdown("### Solución del Rango:")
        st.markdown("El rango de la función es todo $\\mathbb{R}$ excepto $y = 0$.")
        st.latex(r"y \in \mathbb{R}, y \neq 0")
        st.markdown("""
        ### Explicación:
        1. **Dominio**: La función está definida para todos los valores reales excepto $x = 1$ y $x = -1$, porque el denominador se anula en estos puntos.
        2. **Rango**: La función nunca alcanza el valor $y = 0$ debido a la asíntota horizontal.
        """)

        

























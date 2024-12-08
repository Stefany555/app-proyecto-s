
import streamlit as st 


st.title("📊Analisis de funciones racionales ")
st.header("¿Qué es una función?")
st.markdown("""Una función es una relación matemática entre dos conjuntos, de tal manera 
que a cada elemento de un conjunto (llamado dominio) le corresponde exactamente un elemento 
de otro conjunto (llamado codominio).

 una función 𝑓 de un conjunto 𝐴 a un conjunto 𝐵 se denota como:
""")
st.latex(r"f:A→B")

st.markdown("""Lo que significa que la función *f* asigna a cada elemento *x* del conjunto A un unico valor *y* en el
 conjunto B. Este valor *y* se llama **imagen** de x bajo la función *f*, y se denota por $f(x)$.

""")
st.subheader("Propiedades importantes de las funciones:")


st.markdown(r"""
+ **Dominio**: Es el conjunto de todos los valores de entrada posibles para los cuales la función está definida.
    + *Ejemplo*: Para$f(x)= \sqrt{x}$, el dominio es [0,∞), ya que no podemos calcular raíces cuadradas de números negativos en los reales.
    
+ **Codominio**: Es el conjunto de todos los valores posibles de salida de la función, aunque no todos los elementos del
 codominio deben necesariamente estar relacionados con un elemento del dominio.
    + *Ejemplo*: En $f(x)= \ x^2$, el codominio suele considerarse *R* (números reales), aunque los valores negativos no están presentes en la salida.

+ **Imagen o rango**: Es el subconjunto del codominio que contiene todos los valores efectivamente generados por la función.
    + *Ejemplo*: Para $f(x)= \ x^2$ con dominio *R*, la imagen es [0,∞), ya que los cuadrados de números reales no son negativos.

+ **Regla de correspondencia**: Es la fórmula o la relación que describe cómo cada elemento del dominio se asocia con un único elemento del codominio.
    + *Ejemplo*: Para $f(x)= 2x + 1$, la regla de correspondencia indica que cada *𝑥* en el dominio se multiplica por 2 y se le suma 1 para obtener el valor en el codominio.


""")

st.image("https://i.pinimg.com/474x/6f/07/c7/6f07c71a883b2e6eabeff7448b8ff4dc--orice-cus-damato.jpg")
st.header("Funciones Racionales")
st.markdown("""Una función racional es una función matemática que se expresa como el cociente de dos 
polinomios, cumpliendo ciertas condiciones. Formalmente:
""")
st.latex(r"f(x)=\frac{p(x)}{q(x)}")

st.markdown(r"""donde:

+ 1. $P(x)$ y $Q(x)$son polinomios en la variable 𝑥.
+ 2. $Q(x)≠0$ para que la función esté definida.
""")



st.subheader("🧮Representación funciones Racionales:")
st.markdown("""
+ **1. Representación algebraica o analítica:**
Es una expresión matemática explícita que describe cómo se calcula la salida de una función a partir 
de una entrada. Ejemplo:
""")
st.latex(r"f(x)=\frac{x^2+3x-4}{x-2}")


st.markdown(r"""
+ **2. Representación gráfica**
Se utiliza un plano cartesiano para visualizar la relación entre las entradas ($eje  x$) y las salidas 
($eje  y$) Cada punto en el gráfico ($x,y$) cumple la relación establecida por la función. Por ejemplo, la
parábola de $𝑓(𝑥)=𝑥^2$ tiene un vértice en el origen y es simétrica respecto al $eje 𝑦$.""")

st.markdown(r"""
+ **3. Representación tabular**
Se presenta en una tabla donde se indican valores específicos de entrada ($𝑥$) y sus correspondientes 
valores de salida ($𝑓(𝑥$). 
""")


import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import pandas as pd

# Contenedor principal

st.subheader("🧮Ejemplo de graficas y tabla de valores")

# Deslizadores para los coeficientes de la función racional

a = st.slider("Coeficiente a (numerador)", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)
b = st.slider("Coeficiente b (numerador)", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)
c = st.slider("Coeficiente c (denominador)", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)
d = st.slider("Coeficiente d (denominador)", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)

# Generar los valores de x y calcular los correspondientes valores de f(x)
x_values = np.linspace(-10, 10, 21)  # 21 valores de x entre -10 y 10
f_values = np.where(c * x_values + d != 0, (a * x_values + b) / (c * x_values + d), np.nan)  # Evitar división por cero

# Crear una tabla de valores
data = {
    "x": x_values,
    "f(x)": f_values
}

# Convertir a un DataFrame de pandas para mostrar la tabla
df = pd.DataFrame(data)
col1, col2 = st.columns(2)
with col1:
#    Mostrar la tabla
    st.markdown("### Tabla de valores de f(x):")
    st.write(df)
with col2:
    # También se puede mostrar una gráfica de la función
    st.markdown("### Gráfica de la función:")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.plot(x_values, f_values, label=f"f(x) = ({a}x + {b}) / ({c}x + {d})")
    ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
    ax.axvline(0, color='black', linewidth=0.5, linestyle='--')
    ax.grid(True, alpha=0.3)
    ax.legend()
    st.pyplot(fig)













#graficas 

import streamlit as st 
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd 
st.title("graficas:")

#1. crar puntos  
x = [0,1,3,4,5,7]
y = [2,3,3,1,2,5]


#2. creo el canva 
fig, ax = plt.subplots()


#3. dibujo en el canva 
ax.plot(x,y)

#4. configuraciones ( opcional )
ax.grid()


#5. mostrar en steamlit

st.pyplot(fig)

st.divider()

#graficar una funcion 

x = np.linspace(-np.pi, np.pi, 12)
y =np.sin(x)


fig, ax = plt.subplots()
ax.plot(x,y)
ax.grid()


st.pyplot(fig)

# graficar x^2 - 5 
c1, c2 = st.columns([1,2], vertical_aligment="center")

with c1:
    st.markdown("para mostrar diferentes intervalos en la  grafica de la funcion $f(x)=x^2 - 5$ utilice el sigiente slider:")

    xin, xfin = st.slider("interval", min_value=-10, max_value=10, value=(-2, 2))

with c2:
    x = np.linspace(xin, xfin, 100)
    y = x**2 - 5


fig, ax = plt.subplots()
ax.plot(x,y)
ax.grid()

st.pyplot(fig)

st.divider()
st.subheader("graficando figuras ")

puntos = pd.DataFrame({
    "x": [1, 1, -1],
    "y": [1, -1, 0.5],
})

pol = patches.Poligon(puntos, closed=True, fill=True, facecolor="skyblue", edgecolor="navy")

fig, ax = plt.subplots()
ax. add_patch(pol)

ax.set_xlim(puntos["x"].min()-1, puntos["x"].max()+1)
ax.set_xlim(puntos["y"].min()-1, puntos["y"].max()+1)
ax.set_aspect("equal")

st.pyplot(fig)

#inputs

import  streamlit as st

st.title("Página de inputs")

st.slider("")

nombre = st.text_input("Digite su nombre:")
st.markdown(f"el nombre que ingresó es: {nombre}")

edad = st.number_input("digite su edad:", min_value=0, max_value=120)
st.markdown(f"la edad que ingresó es: {edad}")
if edad>18:
    st.markdown("eres mayor de edad")
else:
    st.markdown("eres menor de edad")


rango = st.slider("digite un valor:", min_value=0, max_value=10)
st.markdown(f"el valor que ingresó es: {rango}")

ini, final = st.slider("Seleccione rangos:", min_value=0, max_value=10, value=(2,5))
st.markdown(f"el valor inicial es: {ini} y el valor final es: {final}")




#selección 
x = st.number_input("x:")
y = st.number_input("y:")

opc = st.selectbox("operación:", options=["sumar", "restar", "multiplicar", "dividir"])

if opc == "sumar":
    st.markdown(f"la suma es: {x+y}")
elif opc == "restar":
    st.markdown(f"la resta es: {x-y}")
elif opc == "multiplicar":
    st.markdown(f"la multiplicación es: {x*y}")
elif opc == "dividir":
    st.markdown(f"la división es: {x/y}")

#textos 

import streamlit as st 


st.title("Stefany Blanco")
st.caption(" soy estudiante de matematicas")

st.title("titulo de nvel 1")
st.header("titulo de nivel2")
st.subheader("titulo de nivel 3")



#textos 
st.markdown("""
En una etiqueta tio mardown pueden tener cualqier texto en el formato makdwon.
Podemos poner un texto en **negrilla**, en *italica* o en ***ambos***.

Esto es otra linea 

1. primer item 
2. segundo item 
3. tercer item


items:

+ item 1 
+ item 2
+ item 3

Podemos dar colo al texto por ejemplo :red[rojo], :blue[azul], :green[verde] y asi ...

""")


#ecuaciones 
st.latex("a^2 + b^2 = c^2")

#elemento media:
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSc9wEuFT-XY4L2RvxqKpV3j0gVKeAOzVRTGw&s")

st.video("https://youtu.be/2yfkEAt2ew0?si=ce-Lw4_K3I4GFtk5")

#layout
#container 
with st.container(border=True):
    st.markdown("formula del estudiante:")
    st.latex(r"x = \frac{-b\pm \sqrt{b^2 - 4ac}}{2a}")


#columnas 
c1, c2 = st.columns(2, vertical_alignment="center")

with c1: 
    st.markdown("este texto debe aparecer en la primera columna.")
    st.title("f(x) = x^x")

with c2:
    st.markdown("este texto debe aparecer en la segunda columna.")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSc9wEuFT-XY4L2RvxqKpV3j0gVKeAOzVRTGw&s")





st.title("Analisis de funciones ")
st.header("¿Qué es una función?")
st.markdown("""Una función es una relación matemática entre dos conjuntos, de tal manera que a cada elemento de un conjunto (llamado dominio) le corresponde exactamente un elemento de otro conjunto (llamado codominio).

 una función 𝑓 de un conjunto 𝐴 a un conjunto 𝐵 se denota como:
""")
st.latex(r"f:A→B")

st.markdown("""Lo que significa que la función *f* asigna a cada elemnto *x* del conjunto A un unico valor *y* en el conjunto B. Este valor *y* se llama **imagen** de x bajo la función *f*, y se denota por *f(x)*.
""")

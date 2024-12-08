import streamlit as st
import sympy as sp

st.header("📊 Asíntotas de una función racional")

# Explicación general
st.markdown(r"""
En una **función racional**, las asíntotas son líneas que describen el comportamiento de la función 
cuando \($x$\) tiende a infinito o cuando \($x$\) se acerca a un valor que hace que la función no esté definida.

Existen tres tipos principales de asíntotas:
1. **Asíntota vertical**: Aparece cuando el denominador de la función se hace cero.
2. **Asíntota horizontal**: Se da cuando la función se acerca a un valor constante cuando \($x$\) tiende a infinito.
3. **Asíntota oblicua**: Ocurre cuando la función tiene una pendiente no horizontal cuando \($x$\) tiende a infinito.

""")
st.subheader("¿Cómo hallar las asíntotas?")

st.write(r"""
### 1. **Asíntotas Verticales:**
Las asíntotas verticales ocurren cuando el denominador de la función se hace cero. Para encontrarlas:
- Factoriza el denominador.
- Resuelve la ecuación \( $D(x) = 0$ \), donde \( $D(x)$ \) es el denominador.

### 2. **Asíntotas Horizontales:**
Dependen de los grados relativos del numerador \($N(x)$\) y el denominador \($D(x)$\):
""")

# Ahora usamos st.latex() para las fórmulas y así asegurar su correcta visualización en la página
st.latex(r"""
\text{Si el grado del numerador} < \text{grado del denominador}, \text{ la asíntota horizontal es } y = 0.
""")

st.latex(r"""
\text{Si el grado del numerador es igual al grado del denominador, entonces la asíntota horizontal es } y = \frac{\text{coeficiente líder de } N}{\text{coeficiente líder de } D}.
""")

st.latex(r"""
\text{Si el grado del numerador es mayor que el grado del denominador, entonces no hay asíntota horizontal (puede haber una asíntota oblicua)}.
""")

st.write(r"""
### 3. **Asíntotas Oblícuas:**
3. **Asíntota oblicua**: Si el grado de \($P(x)$\) es mayor que el de \($Q(x)$\), realiza la división polinómica entre \($P(x)$\) y \($Q(x)$\). El cociente, 
sin el residuo, es la ecuación de la asíntota oblicua.
""")

st.subheader("Analizamos la función ")
st.latex(r"f(x) = \frac{2x^2 - 3}{x^2 - 1}")
st.markdown(r"""

1. **Asíntotas Verticales:**  
   El denominador es cero cuando \( $x^2 - 1 = 0$ \), es decir, \( $x = 1$ \) y \( $x = -1$ \).  
   Por lo tanto, hay asíntotas verticales en:
   \[$x = 1 \quad \text{y} \quad x = -1$\]

2. **Asíntotas Horizontales:**  
   Los grados del numerador y denominador son iguales (2). La asíntota horizontal es:     

   \[$y = \frac{\text{coeficiente líder del numerador}}{\text{coeficiente líder del denominador}} = \frac{2}{1} = 2$\]

3. **Asíntotas Oblícuas:**  
   No hay asíntotas oblicuas porque los grados del numerador y denominador son iguales.

Respuestas del análisis:
- **Asíntotas verticales**: \( $x = 1$ \), \( $x = -1$ \).
- **Asíntota horizontal**: \( $y = 2$ \).
""")
st.subheader("Práctica: Encuentra las Asíntotas de una Función")

# Función para el ejercicio
st.latex(r"f(x) = \frac{x^2 + 2x - 3}{x - 1}")
st.write("Selecciona las opciones correctas sobre las asíntotas de esta función:")

# Opciones posibles
options = [
    "Asíntota vertical en x = 1",
    "Asíntota horizontal en y = 0",
    "Asíntota oblicua en y = x + 3",
    "No tiene asíntotas horizontales",
    "No tiene asíntotas oblicuas"
]

# Crear un checkbox para cada opción
selected_options = []
for option in options:
    if st.checkbox(option):
        selected_options.append(option)

# Verificación de las respuestas
if st.button("Verificar respuestas"):
    # Respuestas correctas
    correct_answers = {
        "Asíntota vertical en x = 1",
        "No tiene asíntotas horizontales",
        "Asíntota oblicua en y = x + 3"
    }

    # Comparar selección con las respuestas correctas
    selected_set = set(selected_options)

    # Evaluar si las respuestas son correctas
    if selected_set == correct_answers:
        st.success("¡Correcto! Identificaste todas las asíntotas correctamente.")
    else:
        st.error("Algunas respuestas son incorrectas. Aquí tienes la solución completa:")

        # Explicación de la solución
        st.subheader("Solución")
        st.write("""
        La función es \( f(x) = \frac{x^2 + 2x - 3}{x - 1} \). Al analizarla:

        1. **Asíntota Vertical:**  
           Ocurre donde el denominador es cero. Resolviendo \( x - 1 = 0 \), encontramos que hay una asíntota vertical en:
           \[
           x = 1
           \]

        2. **Asíntota Horizontal:**  
           El grado del numerador (2) es mayor que el grado del denominador (1). Por lo tanto, no hay asíntota horizontal.

        3. **Asíntota Oblicua:**  
           Realizamos la división de polinomios:  
           \[
           \frac{x^2 + 2x - 3}{x - 1} = x + 3 + \frac{0}{x - 1}
           \]  
           Por lo tanto, hay una asíntota oblicua en:
           \[
           y = x + 3
           \]

        **Respuestas correctas:**  
        - Asíntota vertical en \(x = 1\).  
        - No tiene asíntotas horizontales.  
        - Asíntota oblicua en \(y = x + 3\).  
        """)













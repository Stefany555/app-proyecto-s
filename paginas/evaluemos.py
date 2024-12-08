import streamlit as st
import streamlit as st

# Respuestas correctas
correct_answers = {
    "q1": "b",
    "q2": "a",
    "q3": "a",
    "q4": "a",
    "q5": "b",
    "q6": "b",
    "q7": "a",
    "q8": "b",
    "q9": "a",
    "q10": "a",
    "q11": "a",
    "q12": "a",
    "q13": "b",
    "q14": "a",
    "q15": "a",
    "q16": "a",
    "q17": "a",
    "q18": "a",
    "q19": "a",
    "q20": "a",
}

# Función para verificar respuestas
def check_answer(question, answer):
    if answer == correct_answers[question]:
        return "✅ Correcto!"
    else:
        return "❌ Incorrecto."


# Encabezado de la sección de evaluación
st.header("📊 Evaluación📝")

# Instrucciones
st.write("🙏 Por favor, responde las siguientes preguntas sobre funciones racionales y tu experiencia con el sitio.")

# Preguntas sobre funciones racionales
st.subheader("1. Preguntas sobre funciones racionales 🧮")

q1 = st.radio(
    "¿Cómo se determina el dominio de una función racional?",
    ("a) Determinando donde el numerador es 0", 
     "b) Determinando donde el denominador es 0", 
     "c) Calculando la derivada de la función", 
     "d) Ninguna de las anteriores"),
    key="q1"
)

q2 = st.radio(r"¿Cuál es el dominio de \( $f(x) = \frac{1}{x^2 - 4}$ \)?",
    ("a) \( ($-\infty, -2$) \cup ($2, \infty$) \)", 
     "b) \( ($-\infty, \infty$) \)", 
     "c) \( ($-2, 2$) \)", 
     "d) \( $x =0$ \)"),
    key="q2"
)

q3 = st.radio(r"Si la función es \( $f(x) = \frac{2x}{x^2 + 1}$ \), ¿cuál es su rango?",
    ("a) \( ($-\infty, \infty$) \)", 
     "b) \( [$0, \infty$) \)", 
     "c) \( ($-1, 1$) \)", 
     "d) Ninguna de las anteriores"),
    key="q3"
)

q4 = st.radio(
    "¿Cómo se determina el rango de una función racional?",
    ("a) Determinando el comportamiento en los extremos", 
     "b) Hallando los valores de \( $f(x)$ \) para todos los \($ x$ \)", 
     "c) Evaluando el numerador y el denominador", 
     "d) Calculando la derivada de la función"),
    key="q4"
)

q5 = st.radio(
    "¿Qué es una asíntota vertical?",
    ("a) Una línea que describe el comportamiento de la función en los extremos", 
     "b) Una línea donde la función es indefinida", 
     "c) Una línea que cruza el eje y", 
     "d) Ninguna de las anteriores"),
    key="q5"
)

q6 = st.radio(
    "¿Cómo se calcula la posición de una asíntota vertical en una función racional?",
    ("a) Donde el numerador se hace cero", 
     "b) Donde el denominador se hace cero", 
     "c) Evaluando los valores límites de la función", 
     "d) Ninguna de las anteriores"),
    key="q6"
)

q7 = st.radio(
    "¿Cómo se calcula una asíntota horizontal en una función racional?",
    (r"a) Evaluando el límite cuando \( $x   a   \infty$ \)", 
     "b) Buscando los valores del numerador", 
     "c) Si el grado del numerador es mayor que el denominador", 
     "d) Ninguna de las anteriores"),
    key="q7"
)

q8 = st.radio(r"Si \( $f(x) = \frac{1}{x - 2}$ \), ¿dónde tiene una asíntota vertical?",
    ("a) \( $x = 0$ \)", 
     "b) \( $x = 2$ \)", 
     "c) \( $y = 0$ \)", 
     "d) No tiene asíntota vertical"),
    key="q8"
)

q9 = st.radio(
    "¿Cómo se calcula el corte con el eje \( $x$ \) de una función racional?",
    ("a) Hallando los valores de \( $x$ \) donde \( $f(x) = 0$ \)", 
     "b) Hallando los valores donde el numerador es 0", 
     "c) Evaluando el denominador cuando \( $x = 0$ \)", 
     "d) Ninguna de las anteriores"),
    key="q9"
)

q10 = st.radio(r"Si \( $f(x) = \frac{3x + 1}{x - 1}$ \), ¿cuál es su corte con el eje \( $x$ \)?",
    (r"a) \( $x = -\frac{1}{3}$ \)", 
     "b) \( $x = 1$ \)", 
     "c) \( $x = 0$ \)", 
     "d) No tiene corte con el eje \( $x$ \)"),
    key="q10"
)

q11 = st.radio(
    "¿Qué es un corte con el eje \( y \) en una función racional?",
    ("a) El valor de \( f(x) \) cuando \( x = 0 \)", 
     "b) El valor de \( x \) cuando \( f(x) = 0 \)", 
     "c) El valor de la derivada en \( x = 0 \)", 
     "d) Ninguna de las anteriores"),
    key="q11"
)

q12 = st.radio(r"Si \( $f(x) = \frac{4}{x^2 - 1}$ \), ¿qué valor tiene el corte con el eje \( $y$ \)?",
    ("a) \( $f(0) = 4$ \)", 
     "b) \( $f(0) = 0$ \)", 
     "c) No tiene corte con el eje \( $y$ \)", 
     "d) \( $f(0) = -4$ \)"),
    key="q12"
)

q13 = st.radio(
    "¿Qué pasa si el numerador y el denominador tienen un factor común en una función racional?",
    ("a) La función tiene un corte con el eje \( x \)", 
     "b) Hay una discontinuidad removible", 
     "c) La función tiene una asíntota horizontal", 
     "d) Ninguna de las anteriores"),
    key="q13"
)

q14 = st.radio(
    "¿Qué se debe hacer cuando la función tiene un factor común entre el numerador y denominador?",
    ("a) Eliminar el factor común", 
     "b) Multiplicar el numerador por el denominador", 
     "c) Dividir el numerador por el denominador", 
     "d) Ninguna de las anteriores"),
    key="q14"
)

q15 = st.radio(r"Si \( $f(x) = \frac{x - 1}{x^2 - 4}$ \), ¿qué valor tiene el corte con el eje \( $y$ \)?",
    ("a) \( $f(0) = 1$ \)", 
     "b) \( $f(0) = -1$ \)", 
     "c) \( $f(0) = 0$ \)", 
     "d) \( $f(0) = 2$ \)"),
    key="q15"
)

# Preguntas sobre la experiencia del usuario
st.subheader("2. Preguntas sobre la página web 🌐")

q16 = st.radio(
    "¿Cómo calificarías el diseño visual de la página?",
    ("a) Muy bueno 😊", "b) Bueno 🙂", "c) Aceptable 😐", "d) Malo 😞"),
    key="q16"
)

q17 = st.radio(
    "¿Qué tan fácil fue encontrar la información que necesitabas?",
    ("a) Muy fácil 😃", "b) Fácil 🙂", "c) Difícil 😕", "d) Muy difícil 😩"),
    key="q17"
)

q18 = st.radio(
    "¿Qué tan útil fue la página para aprender sobre funciones racionales?",
    ("a) Muy útil 📘", "b) Útil 👍", "c) Algo útil 🤔", "d) No útil 👎"),
    key="q18"
)

q19 = st.radio(
    "¿La página cargó rápidamente?",
    ("a) Sí 🚀", "b) No ⏳", "c) A veces ⚡", "d) No sé 🤷‍♂️"),
    key="q19"
)

q20 = st.radio(
    "¿Recomendarías esta página a otros estudiantes?",
    ("a) Sí, definitivamente 👍", "b) Sí, probablemente 🙂", "c) No estoy seguro 🤔", "d) No 😕"),
    key="q20"
)

if st.button("Enviar evaluación 🚀"):
    # Mostrar respuestas de funciones racionales
    st.write("### Resultados de las preguntas sobre funciones racionales 🧮")
    st.write(f"Pregunta 1: {q1} - {check_answer('q1', q1)}")
    st.write(f"Pregunta 2: {q2} - {check_answer('q2', q2)}")
    st.write(f"Pregunta 3: {q3} - {check_answer('q3', q3)}")
    st.write(f"Pregunta 4: {q4} - {check_answer('q4', q4)}")
    st.write(f"Pregunta 5: {q5} - {check_answer('q5', q5)}")
    st.write(f"Pregunta 6: {q6} - {check_answer('q6', q6)}")
    st.write(f"Pregunta 7: {q7} - {check_answer('q7', q7)}")
    st.write(f"Pregunta 8: {q8} - {check_answer('q8', q8)}")
    st.write(f"Pregunta 9: {q9} - {check_answer('q9', q9)}")
    st.write(f"Pregunta 10: {q10} - {check_answer('q10', q10)}")
    st.write(f"Pregunta 11: {q11} - {check_answer('q11', q11)}")
    st.write(f"Pregunta 12: {q12} - {check_answer('q12', q12)}")
    st.write(f"Pregunta 13: {q13} - {check_answer('q13', q13)}")
    st.write(f"Pregunta 14: {q14} - {check_answer('q14', q14)}")
    st.write(f"Pregunta 15: {q15} - {check_answer('q15', q15)}")

    # Mostrar respuestas de la experiencia del usuario


   
    st.success("¡Gracias por tu evaluación! 🎉")
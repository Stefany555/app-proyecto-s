import streamlit as st

#1) crear las páginas 
txts = st.Page("paginas/Introducción.py", title= "Introducción", icon=":material/text_fields:")
inps = st.Page("paginas/Presentación.py", title= "Presentación", icon=":material/person_alert:")
ejs = st.Page("paginas/Dominio y Rango.py", title= "Dominio y rango", icon=":material/swipe_left:")
graphs = st.Page("paginas/asintotas.py", title= "Asíntotas", icon=":material/bottom_right_click:")
fs = st.Page("paginas/funciones.py", title= "Cortes con los ejes ", icon=":material/prescriptions:")
ev = st.Page("paginas/evaluemos.py", title= "Evaluemos", icon=":material/psychology_alt:")
vi = st.Page("paginas/videos.py", title= "Videos", icon=":material/subscriptions:")

#2) crear la navegación
#pg = st.navigation([txts, imps, ejs])
pg = st.navigation({"Inicio": [inps, txts], "Propiedades": [ejs, graphs, fs, vi, ev]})
#3) ejecutar
pg.run()
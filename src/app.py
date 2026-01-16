import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("EMPLEATRONIX")
st.write("Todos los datos sobre los empleados en una aplicación.")

df = pd.read_csv("employees.csv")

df

st.divider()

with st.container(horizontal=True):
    color = st.color_picker("Elige un color para las barras", "#3475B3")
    nombre = st.toggle("Mostrar el nombre", value=True)
    sueldo = st.toggle("Mostrar sueldo en la barra")


fig, ax = plt.subplots()
y_pos = np.arange(len(df["full name"]))

bars = ax.barh(
    y_pos, 
    df["salary"], 
    align='center', 
    color=color
)

if(nombre):
    etiqueta_y = df["full name"]
else:
    etiqueta_y = ""

ax.set_yticks(y_pos, labels=etiqueta_y)
ax.set_xlim(0, 4500)

if(sueldo):
    ax.bar_label(
    bars,
    labels=[f"{v} €" for v in df["salary"]],
    padding=3
)
    
ax.tick_params(axis='x', labelrotation=90)

st.pyplot(fig)

st.write("© Antonio Delgado Rodríguez - CPIFP Alan Turing")

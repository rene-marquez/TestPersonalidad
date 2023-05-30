"""
import streamlit as st

some_list = [1, 2, 3, 4, 5]

def get_data(key: int):
    return st.session_state["data"].get(key, None)


def add_data(key: int, value: int):
    st.session_state["data"][key] = value


for e in some_list:
    result = get_data(e)
    if not result:
        new_value = st.text_input(f"Missing value for {e}")
        tmp_button = st.button("Add value to database", key=f"missing_{e}")
        if tmp_button:
            add_data(e, new_value)
            st.experimental_rerun()
        else:
            st.stop()

    st.write(e, "=", st.session_state["data"][e])
"""
import streamlit as st
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import requests
import seaborn as sns
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import psycopg2

# Solicitar el nombre por teclado
st.text_input("¿Cuál es tu nombre?:", key="nombre")
userName = st.session_state.nombre
if not userName:
  st.warning("Por favor captura un nombre.")
  st.stop()
st.success("Gracias.")

# Solicitar el identificador por teclado
st.text_input("¿Cuál es el Id del resultado del test de la pagina https://bigfive-test.com/es?:", key="identificador")
identificador = st.session_state.identificador
if not identificador:
  st.warning("Por favor captura un identificador.")
  st.stop()
elif len(identificador)!=24:
  st.warning("Por favor, verifica el identificador del resultado del test.")
  st.stop()
else:
   while True:
    # Concatenar el identificador a la URL base del sitio web
    url = f"https://bigfive-test.com/result/{identificador}"

    # Obtener la respuesta HTTP de la URL

    response = requests.get(url)

    # Buscar la frase ""Request failed with status code 500"" en la URL    
    if "Request failed with status code 500" in response.text:
     st.warning("La URL no es válida. Por favor, verifica el identificador del resultado del test.")
     st.stop()
     if not identificador: 
        st.warning("Por favor captura un identificador.")
        st.stop()
     #st.success("Gracias.")
     
    else:
     # Crear el objeto soup object desde response
     soup = BeautifulSoup(response.content, "html.parser")
     
     break
st.success("Gracias.")
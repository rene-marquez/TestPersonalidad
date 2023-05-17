import streamlit as st
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import requests
import seaborn as sns
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Solicitar el nombre por teclado
st.text_input("¿Cuál es tu nombre?:", key="nombre")
userName = st.session_state.nombre
# Solicitar el identificador por teclado
st.text_input("¿Cuál es el Id del resultado del test?:", key="identificador")
identificador = st.session_state.identificador

while True:
    # Concatenar el identificador a la URL base del sitio web
    url = f"https://bigfive-test.com/result/{identificador}"

    # Obtener la respuesta HTTP de la URL

    response = requests.get(url)

    # Buscar la frase ""Request failed with status code 500"" en la URL    
    if "Request failed with status code 500" in response.text:
     identificador = input("La URL no es válida. Por favor, verifica el identificador del resultado del test.")
    else:
     # Crear el objeto soup object desde response
     soup = BeautifulSoup(response.content, "html.parser")
     break


# Definiendo la lista de atributos a extraer
atributos = ["Neurosis", "Ansiedad", "Ira", "Depresión", "Vergüenza", 
              "Falta de moderacion", "Vulnerabilidad", "Extroversión", 
              "Cordialidad", "Sociabilidad", "Confianza", "Nivel de actividad", 
              "Búsqueda de nuevas experiencias", "Alegría", "Apertura a experiencias", 
              "Imaginación", "Interes artístico", "Sensibilidad", "Ansias de aventura", 
              "Intelecto", "Liberalismo", "Simpatía", "Confianza", "Moral", "Altruismo", 
              "Cooperación", "Modestia", "Empatía", "Meticulosidad", "Autoeficacia", 
              "Orden", "Sentido del deber", "Orientación a objetivos", "Disciplina", "Prudencia"]

# Creando una lista para almacenar los resultados
resultados = [identificador, userName.title()]

# loop over the attributes and extract the corresponding scores
for atributo in atributos:
    # find the corresponding div
    div = soup.find("a", {"href": f"#{atributo.lower()}"})
    # extract the score
    score = div.find_next('p').text.split(":")[1].strip()
    # Validando que el resultado a extraer sean solo dos digitos
    if score[3] == "-":
        score = int(score[:2])
    else:        
        # Validando que el resultado a extraer sean solo un digito
        if score[2] == "-":
            score = int(score[:1])
        # Validando que el resultado a extraer sean tres digitos
        else:
            score = int(score[:3])   
        
    # append the attribute name and score to the results list
    resultados.append(score)    

# create a pandas DataFrame from the results list

testPersonalidad = pd.DataFrame([resultados], columns=["Identificador", "Nombre","Neurosis", "Ansiedad", "Ira", "Depresión", "Vergüenza", 
                                                        "Falta de moderacion", "Vulnerabilidad", "Extroversión", 
                                                        "Cordialidad", "Sociabilidad", "Confianza", "Nivel de actividad", 
                                                        "Búsqueda de nuevas experiencias", "Alegría", "Apertura a experiencias", 
                                                        "Imaginación", "Interes artístico", "Sensibilidad", "Ansias de aventura", 
                                                        "Intelecto", "Liberalismo", "Simpatía", "Confianza 2", "Moral", "Altruismo", 
                                                        "Cooperación", "Modestia", "Empatía", "Meticulosidad", "Autoeficacia", 
                                                        "Orden", "Sentido del deber", "Orientación a objetivos", "Disciplina", "Prudencia"
                                                         ])
st.write("Here's our first attempt at using data to create a table:")

st.dataframe(testPersonalidad)
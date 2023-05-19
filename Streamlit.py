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

st.dataframe(testPersonalidad)

#Creando la grafica radial con los resultados principales
st.write("Este es el resultado del \"The big 5\":")
datos5 = testPersonalidad.loc[:, ["Neurosis", "Extroversión", "Apertura a experiencias", "Simpatía", "Meticulosidad"]]

etiquetas=['Neurosis', 'Extroversión', 'Apertura a experiencias', 'Simpatía', 'Meticulosidad']

lista = list(datos5.iloc[0])
lista=np.concatenate((lista, [lista[0]]))
esperado = (60, 80, 70, 60, 80, 60)


plt.figure(figsize =(10, 6))
plt.subplot(polar = True)

theta = np.linspace(0, 2 * np.pi, len(lista))

lineas, labels = plt.thetagrids(range(0, 360, int(360/len(etiquetas))),
                                                         (etiquetas))
plt.plot(theta, esperado)
plt.plot(theta, lista)
plt.fill(theta, lista, 'b', alpha = 0.1)
plt.legend(labels =("Prospecto", userName.title()), loc = 3, framealpha=1)
st.pyplot(plt.gcf())

#Creando la grafica radial con los resultados de neurosis
st.write("Este es el resultado de Neurosis:")
neurosis = testPersonalidad.loc[:, ["Ansiedad", "Ira", "Depresión", "Vergüenza", 
                                      "Falta de moderacion", "Vulnerabilidad"]]
etiquetas=["Ansiedad", "Ira", "Depresión", "Vergüenza", "Falta de moderacion", "Vulnerabilidad"]

lista = list(neurosis.iloc[0])
lista=np.concatenate((lista, [lista[0]]))
esperado = (10, 10, 10, 10, 10, 10, 10)

plt.figure(figsize =(10, 6))
plt.subplot(polar = True)
theta = np.linspace(0, 2 * np.pi, len(lista))
lineas, labels = plt.thetagrids(range(0, 360, int(360/len(etiquetas))),
                                                         (etiquetas))
plt.plot(theta, esperado)
plt.plot(theta, lista)
plt.fill(theta, lista, 'b', alpha = 0.1)
plt.legend(labels =("Prospecto", userName.title()), loc = 3, framealpha=0)
st.pyplot(plt.gcf())

#Creando la grafica radial con los resultados de extroversión
st.write("Este es el resultado de Extroversión:")
extroversion = testPersonalidad.loc[:, ["Cordialidad", "Sociabilidad", "Confianza", "Nivel de actividad", 
                                                        "Búsqueda de nuevas experiencias", "Alegría"]]
etiquetas=["Cordialidad", "Sociabilidad", "Confianza", "Nivel de actividad", 
            "Búsqueda de nuevas experiencias", "Alegría"]

lista = list(extroversion.iloc[0])
lista=np.concatenate((lista, [lista[0]]))
esperado = (10, 10, 10, 10, 10, 10, 10)

plt.figure(figsize =(10, 6))
plt.subplot(polar = True)
theta = np.linspace(0, 2 * np.pi, len(lista))
lineas, labels = plt.thetagrids(range(0, 360, int(360/len(etiquetas))),
                                                         (etiquetas))
plt.plot(theta, esperado)
plt.plot(theta, lista)
plt.fill(theta, lista, 'b', alpha = 0.1)
plt.legend(labels =("Prospecto", userName.title()), loc = 3, framealpha=0)
st.pyplot(plt.gcf())

#Creando la grafica radial con los resultados de apertura a experiencias
st.write("Este es el resultado de Apertura a Experiencias:")
aperturaExperiencias = testPersonalidad.loc[:, ["Imaginación", "Interes artístico", "Sensibilidad", "Ansias de aventura", 
                                                        "Intelecto", "Liberalismo"]]
etiquetas=["Imaginación", "Interes artístico", "Sensibilidad", "Ansias de aventura", 
                                                        "Intelecto", "Liberalismo"]
lista = list(extroversion.iloc[0])
lista=np.concatenate((lista, [lista[0]]))
esperado = (10, 10, 10, 10, 10, 10, 10)

plt.figure(figsize =(10, 6))
plt.subplot(polar = True)
theta = np.linspace(0, 2 * np.pi, len(lista))
lineas, labels = plt.thetagrids(range(0, 360, int(360/len(etiquetas))),
                                                         (etiquetas))
plt.plot(theta, esperado)
plt.plot(theta, lista)
plt.fill(theta, lista, 'b', alpha = 0.1)
plt.legend(labels =("Prospecto", userName.title()), loc = 3, framealpha=0)
st.pyplot(plt.gcf())

#Creando la grafica radial con los resultados de simpatia
st.write("Este es el resultado de Simpatia:")
simpatia = testPersonalidad.loc[:, ["Confianza 2", "Moral", "Altruismo", 
                                    "Cooperación", "Modestia", "Empatía"]]
etiquetas=["Confianza", "Moral", "Altruismo", "Cooperación", "Modestia", "Empatía"]

lista = list(simpatia.iloc[0])
lista=np.concatenate((lista, [lista[0]]))
esperado = (10, 10, 10, 10, 10, 10, 10)

plt.figure(figsize =(10, 6))
plt.subplot(polar = True)
theta = np.linspace(0, 2 * np.pi, len(lista))
lineas, labels = plt.thetagrids(range(0, 360, int(360/len(etiquetas))),
                                                         (etiquetas))
plt.plot(theta, esperado)
plt.plot(theta, lista)
plt.fill(theta, lista, 'b', alpha = 0.1)
plt.legend(labels =("Prospecto", userName.title()), loc = 1, framealpha=0)
st.pyplot(plt.gcf())

#Creando la grafica radial con los resultados de Meticulosidad
st.write("Este es el resultado de Meticulosidad:")
meticulosidad = testPersonalidad.loc[:, ["Autoeficacia", "Orden", "Sentido del deber", 
                                         "Orientación a objetivos", "Disciplina", "Prudencia"]]
etiquetas=["Autoeficacia", "Orden", "Sentido del deber", "Orientación a objetivos", "Disciplina", "Prudencia"]

lista = list(meticulosidad.iloc[0])
lista=np.concatenate((lista, [lista[0]]))
esperado = (10, 10, 10, 10, 10, 10, 10)

plt.figure(figsize =(10, 6))
plt.subplot(polar = True)
theta = np.linspace(0, 2 * np.pi, len(lista))
lineas, labels = plt.thetagrids(range(0, 360, int(360/len(etiquetas))),
                                                         (etiquetas))
plt.plot(theta, esperado)
plt.plot(theta, lista)
plt.fill(theta, lista, 'b', alpha = 0.1)
plt.legend(labels =("Prospecto", userName.title()), loc = 3, framealpha=0)
st.pyplot(plt.gcf())
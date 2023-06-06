import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import psycopg2

table_name = "test"
#Haciendo la conexión a la BD
conn = psycopg2.connect(database="personality_test",
                        host="138.197.196.136",
                        user="persontest",
                        password="f57403cdcca683e5b",
                        port="5432")

cursor = conn.cursor()
#Seleccionando todos los datos de la BD
select_query = f"SELECT * FROM {table_name}"
cursor.execute(select_query)
registros = cursor.fetchall()
#Creando el template del dataframe
testPersonalidad = pd.DataFrame(columns=["Identificador", "Nombre","Neurosis", "Ansiedad", "Ira", "Depresión", "Vergüenza", 
                                                        "Falta de moderacion", "Vulnerabilidad", "Extroversión", 
                                                        "Cordialidad", "Sociabilidad", "Confianza", "Nivel de actividad", 
                                                        "Búsqueda de nuevas experiencias", "Alegría", "Apertura a experiencias", 
                                                        "Imaginación", "Interes artístico", "Sensibilidad", "Ansias de aventura", 
                                                        "Intelecto", "Liberalismo", "Simpatía", "Confianza 2", "Moral", "Altruismo", 
                                                        "Cooperación", "Modestia", "Empatía", "Meticulosidad", "Autoeficacia", 
                                                        "Orden", "Sentido del deber", "Orientación a objetivos", "Disciplina", "Prudencia"
                                                         ])
#Vaciando los datos de la BD al dataframe 
indice=0
for registro in registros:
    testPersonalidad.loc[indice] = registro
    indice += 1      

#Creando la lista de promedio de cada columna
listaPromedio=[]
totalColumnas=len(testPersonalidad.columns)
e=0
while e <= totalColumnas:    
    if e >= 2 and e < 37:
     promedio= (sum(testPersonalidad.iloc[:, e])/(testPersonalidad.index[-1]+1))
     listaPromedio.append(promedio)
    e+=1
    
#Creando el dataframe de promedio
dfPromedio = pd.DataFrame([listaPromedio], columns=["Neurosis", "Ansiedad", "Ira", "Depresión", "Vergüenza", 
                                                        "Falta de moderacion", "Vulnerabilidad", "Extroversión", 
                                                        "Cordialidad", "Sociabilidad", "Confianza", "Nivel de actividad", 
                                                        "Búsqueda de nuevas experiencias", "Alegría", "Apertura a experiencias", 
                                                        "Imaginación", "Interes artístico", "Sensibilidad", "Ansias de aventura", 
                                                        "Intelecto", "Liberalismo", "Simpatía", "Confianza 2", "Moral", "Altruismo", 
                                                        "Cooperación", "Modestia", "Empatía", "Meticulosidad", "Autoeficacia", 
                                                        "Orden", "Sentido del deber", "Orientación a objetivos", "Disciplina", "Prudencia"
                                                         ]) 

option = st.selectbox("¿Cuál es el resultado que quieres revisar?", testPersonalidad["Nombre"])
"Seleccionaste: ", option

st.write(testPersonalidad.loc[(testPersonalidad["Nombre"]==option)])



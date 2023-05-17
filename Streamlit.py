import streamlit as st
import pandas as pd
import numpy as np

# Solicitar el nombre por teclado
st.text_input("¿Cuál es tu nombre?:", key="nombre")
userName = st.session_state.nombre
# Solicitar el identificador por teclado
st.text_input("¿Cuál es el Id del resultado del test?:", key="identificador")
identificador = st.session_state.identificador
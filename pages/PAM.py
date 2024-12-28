import streamlit as st

st.page_link("MdCalculator.py",icon="🩺")

st.title("🎰Calculadora de PAM")
st.write("Esta es una calculadora para calcular presion arterial media")

st.divider()

contenedor = st.container(border=True)
sistolica = contenedor.number_input("Sistolica", value=1)
diastolica = contenedor.number_input("Diastolica", value=1)
media = (sistolica*.33)+(diastolica*.66)
resultado = "🩺 La presion arterial media es 🦾 " + str(int(media)) 
st.error(resultado)

col1, col2, col3 = st.columns(3)
#with col1:
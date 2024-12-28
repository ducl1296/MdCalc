import streamlit as st

st.set_page_config(
    page_title="🩺 MdCalculator",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("🩺 MdCalculator")

col1, col2, col3 = st.columns(3)
with col1:
    st.page_link("pages/BalanceHidrico.py", label="Balance Hidrico", icon="🚰")
with col2:
    st.page_link("pages/PAM.py", label="PAM", icon="🎰") 

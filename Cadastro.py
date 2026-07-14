import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="Cadastro de clientes",
    page_icon=" :bar_chart:",               
)

def gravar_dados(nome, data_nasc, tipo):
    if nome and data_nasc <= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome},{data_nasc},{tipo}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False


st.title("Cadastro de clientes")

@st.cache_data
def carregar_clientes():
    clientes = pd.read_csv('clientes.csv')
    return clientes

clientes = carregar_clientes()
st.session_state["clientes"] = clientes

nome = st.text_input("Digite o nome do cliente", key="nome_cliente")

data_nasc = st.date_input("Data nascimento", format="DD/MM/YYYY")

tipo = st.selectbox("Tipo do cliente", ["Pessoa Física", "Pessoa Jurídica"])

btn_cadastrar = st.button("Cadastrar", on_click=gravar_dados, args=[nome, data_nasc, tipo])

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cadastro realizado com sucesso", icon="✅")
    else:
        st.error("Cadastro não realizado", icon="🚫")
        
        
dados = pd.read_csv("clientes.csv")

st.divider()
st.title("Clientes cadastrados")

st.dataframe(dados)
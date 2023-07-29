import streamlit as st

st.set_page_config(
     page_title="CamVote - Sobre",
     page_icon="📝",
     layout="wide",
     initial_sidebar_state="expanded",
)

imagem = "marca_cesar_school.png"
st.sidebar.image(imagem, use_column_width=False, width=100)

st.header("📝 Sobre")

texto = """
    <p style="text-align: justify;">
    Este é um projeto desenvolvido por <strong>Arthur Lira</strong> e <strong>Filipe Pontes</strong> para a disciplina de Análise e Visualização de 
    Dados da Pós-Graduação de <strong>Engenharia e Análise de Dados</strong> da <strong>CESAR School</strong>, turma 2023.1.
    </p>
    """
    
st.markdown(texto, unsafe_allow_html=True)



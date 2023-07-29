import streamlit as st

st.set_page_config(
     page_title="CamVote - Sobre",
     page_icon="📝",
     layout="wide",
     initial_sidebar_state="expanded",
)

col1, col2, col3 = st.columns([40, 15, 40])

with col1:
    st.write('')
with col2:
    image_url = "marca_cesar_school.png"
    st.image(image_url, use_column_width=True)
with col3:
    st.write('')

st.header("📝 Sobre")

texto = """
    <p style="text-align: justify;">
    Este é um projeto desenvolvido por <strong>Arthur Lira</strong> e <strong>Filipe Pontes</strong> para a disciplina de Análise e Visualização de 
    Dados da Pós-Graduação de <strong>Engenharia e Análise de Dados</strong> da <strong>CESAR School</strong>, turma 2023.1.
    </p>
    """
    
st.markdown(texto, unsafe_allow_html=True)



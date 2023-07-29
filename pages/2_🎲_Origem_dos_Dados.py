import streamlit as st

st.set_page_config(
    page_title="CamVote - Origem dos Dados",
    page_icon="🎲",
    layout="wide",
    initial_sidebar_state="expanded",
)

imagem = "marca_cesar_school.png"
st.sidebar.image(imagem, use_column_width=False, width=100)

st.header("🎲 Origem dos Dados")

st.subheader("Dataset")

texto = """
    <p style="text-align: justify;">
    Os dados foram extraídos através do site da <strong>Câmara dos Deputados</strong>. (<a href="https://www2.camara.leg.br/atividade-legislativa/plenario/relatorios-da-atividade-legislativa/dados-de-votacoes-nominais" target="_blank">link</a>)
    </p>
    """

st.markdown(texto, unsafe_allow_html=True)

st.subheader("Imagens dos Parlamentares")

texto2 = """
    <p style="text-align: justify;">
    As imagens dos parlamentares foram extraídas diretamente do site da Câmara dos Deputados. (<a href="https://www.camara.leg.br/deputados/quem-sao">link</a>)
    </p>
    """

st.markdown(texto2, unsafe_allow_html=True)
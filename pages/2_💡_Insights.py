import streamlit as st

st.set_page_config(
     page_title="CamVote - Insights",
     page_icon="💡",
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

st.header("💡 Insights")
    
texto = """
    <p style="text-align: justify;">
    Através do dashboard e dos gráficos que podem ser gerados a partir dos filtros, podemos perceber uma distribuição partidária bem interessante:\n
    1) A pauta econômica (reforma tributária, arcabouço fiscal) recebeu apoio dos partidos de centro e centro-direita, como PP, PSD, Republicanos e União Brasil; \n
    2) No entanto, o marco temporal das terras indígenas dividiu a Câmara entre direita e esquerda e mesmo partidos com ministérios no governo Lula votaram a favor do projeto, o qual o governo se posicionou contra;\n
    3) Entre os partidos com ministérios no governo, o PSOL, partido mais à esquerda com representação parlamentar, foi o que proporcionalmente menos apoiou a reforma tributária.
    </p>
    """
    
st.markdown(texto, unsafe_allow_html=True)
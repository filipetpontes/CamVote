import streamlit as st

st.set_page_config(
     page_title="CamVote - Contato",
     page_icon="📞",
     layout="wide",
     initial_sidebar_state="expanded",
)

col1, col2, col3 = st.sidebar.columns(3)

with col1:
    st.write('')
with col2:
    image_url = "marca_cesar_school.png"
    st.image(image_url, use_column_width=True)
with col3:
    st.write('')

st.header("📞 Contato")

st.markdown("#### Arthur Lira")
st.markdown("[![Linkedin](https://img.shields.io/badge/LinkedIn-blue)](https://www.linkedin.com/in/arthur-santos-lira-084292145/)")
st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-gray)](https://github.com/arthurrslira/)")

st.markdown("#### Filipe Pontes")
st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue)](https://www.linkedin.com/in/filipetpontes/)")
st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-gray)](https://github.com/filipetpontes)")

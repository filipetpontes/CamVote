import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
     page_title="CamVote",
     page_icon="🏠",
     layout="wide",
     initial_sidebar_state="expanded",
)

df = pd.read_excel('camara_deputados_votacoes_nominais_2023.xlsx', header=[0, 1])
parlamentares = sorted(df['Votação', 'Parlamentar'].unique())
partidos_unicos = sorted(df['Unnamed: 0_level_0', 'Partido'].unique())

col1, col2, col3 = st.columns([40, 15, 40])

with col1:
    st.write('')
with col2:
    image_url = "marca_cesar_school.png"
    st.image(image_url, use_column_width=True)
with col3:
    st.write('')

st.markdown(
"<h2 style='text-align: center; background-color: #307c5c; color: white; padding: 16px;'>Votações Nominais na Câmara dos Deputados - 2023</h2>",
unsafe_allow_html=True
)

projetos = df.columns.get_level_values(0)[2:].unique()
df_projetos = pd.DataFrame(projetos, columns=['projeto'])

df_projetos['projeto_data'] = df_projetos['projeto'].apply(lambda x: x.split("-", 1)[0].strip())
df_projetos['projeto_nome'] = df_projetos['projeto'].apply(lambda x: x.split("-", 1)[1].strip())

projetos_principais = [
    ('Reforma Tributária - 1º Turno', '06/07/2023 21:00:48 - PEC  Nº 45/2019 - SUBSTITUTIVO OFERECIDO PELA COMISSÃO ESPECIAL'),
    ('Reforma Tributária - 2º Turno', '07/07/2023 01:17:05 - PEC  Nº 45/2019 - PROPOSTA DE EMENDA À CONSTITUIÇÃO - 2º TURNO'),
    ('Arcabouço Fiscal', '23/05/2023 23:12:45 - PLP  Nº 93/2023 - SUBSTITUTIVO OFERECIDO PELO RELATOR'),
    ('Marco Temporal das Terras Indígenas', '30/05/2023 20:02:55 - PL   Nº 490/2007 - SUBEMENDA SUBSTITUTIVA'),
    ('MP dos Ministérios', '31/05/2023 22:43:56 - MPV  Nº 1154/2023 - PARECER DA C.M P/ ATEND. DOS PRESSUPOSTOS CONSTITUCIONAIS...'),
    ('Suspensão dos decretos de saneamento emitidos por Lula', '03/05/2023 20:37:16 - PDL  Nº 98/2023 - SUBSTITUTIVO OFERECIDO PELO RELATOR')
]

primeiros_valores = [tupla[0] for tupla in projetos_principais]

st.subheader('Projeto:')

projeto_selecionado2 = st.selectbox('Selecione o projeto', primeiros_valores)

st.subheader('Partidos:')

if st.checkbox("Todos", value=True):
    partidos_selecionados = partidos_unicos
else:
    partidos_selecionados = st.multiselect('Selecione os partidos', partidos_unicos, default=partidos_unicos)

st.subheader('Parlamentares:')

# Filtrar os parlamentares com base nos partidos selecionados
parlamentares_selecionados = df.loc[df[('Unnamed: 0_level_0', 'Partido')].isin(partidos_selecionados), ('Votação', 'Parlamentar')].unique()
selecionar_parlamentar = st.selectbox('Selecione um parlamentar', ['Todos'] + sorted(parlamentares_selecionados))
parlamentar_selecionado = [selecionar_parlamentar]

if selecionar_parlamentar == 'Todos':
    parlamentar_selecionado = parlamentares
else:
    parlamentar_selecionado = [selecionar_parlamentar]

for tupla in projetos_principais:
    if tupla[0] == projeto_selecionado2:
        projeto_selecionado = tupla[1]
        break

df2 = df[['Unnamed: 0_level_0', 'Votação', projeto_selecionado]]

df_filtrado = df2[
    (df2[('Unnamed: 0_level_0', 'Partido')].isin(partidos_selecionados)) &
    (df2[('Votação', 'Parlamentar')].isin(parlamentar_selecionado))
]

if not parlamentar_selecionado:
    st.markdown("Nenhum parlamentar encontrado.")

df_filtrado.columns = ["Partido", "Parlamentar", "Voto", "Orientação"]

df_filtrado = df_filtrado[df_filtrado['Voto'] != '-']

st.markdown(projeto_selecionado)

st.dataframe(df_filtrado, hide_index=True, width=800)

grouped_data = df_filtrado.groupby(["Partido", "Voto"]).size().unstack(fill_value=0)

party_sums = grouped_data.sum(axis=1)
sorted_parties = party_sums.sort_values(ascending=False).index

sorted_data = grouped_data.loc[sorted_parties]

percentages = sorted_data.apply(lambda row: (row / row.sum())*100, axis=1).round(2)

df_long = percentages.reset_index().melt(id_vars='Partido', var_name='Voto', value_name='Percentual')

colors = alt.Scale(domain=['Sim', 'Não', 'Não votou', 'Abstenção'],
                  range=['#90EE90', '#FFA07A', '#D3D3D3', '#D2B48C'])

chart = alt.Chart(df_long).mark_bar().encode(
    x='Partido',
    y='Percentual',
    color=alt.Color('Voto', scale=colors),
    tooltip=['Partido', 'Voto', 'Percentual']
).properties(
    width=600,
    height=400
)

st.altair_chart(chart, use_container_width=True)
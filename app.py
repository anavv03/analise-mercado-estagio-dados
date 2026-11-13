import html

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Mercado de Dados em Portugal", layout="wide")

TINTA = "#1F2933"
TINTA_SUAVE = "#6B7280"
FUNDO = "#F7F5F1"
CARTAO = "#FFFFFF"
LINHA = "#E5E1DA"
DESTAQUE = "#0F766E"
DESTAQUE_SUAVE = "#9CC9C4"

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=Inter:wght@400;500;600&display=swap');

    html, body, [class*="css"], .stApp {{
        font-family: 'Inter', sans-serif;
        color: {TINTA};
    }}
    .stApp {{ background: {FUNDO}; }}
    .block-container {{ padding-top: 2.5rem; max-width: 1200px; }}
    #MainMenu, footer {{ visibility: hidden; }}

    h1, h2, h3 {{ font-family: 'Fraunces', serif !important; font-weight: 600 !important; letter-spacing: -0.01em; }}
    h1 {{ font-size: 2.3rem !important; margin-bottom: 0.2rem; }}
    h3 {{ font-size: 1.15rem !important; margin-bottom: 0.2rem; }}
    .sub {{ color: {TINTA_SUAVE}; font-size: 1rem; margin-bottom: 1.8rem; max-width: 640px; }}

    section[data-testid="stSidebar"] {{ background: {CARTAO}; border-right: 1px solid {LINHA}; }}

    .kpi {{
        background: {CARTAO};
        border: 1px solid {LINHA};
        border-radius: 10px;
        padding: 1.1rem 1.3rem;
    }}
    .kpi-label {{ font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em; color: {TINTA_SUAVE}; }}
    .kpi-value {{ font-family: 'Fraunces', serif; font-size: 2rem; font-weight: 600; line-height: 1.2; margin-top: 0.25rem; }}
    .kpi-sub {{ font-size: 0.85rem; color: {DESTAQUE}; margin-top: 0.1rem; min-height: 1.2rem; }}

    .painel {{
        background: {CARTAO};
        border: 1px solid {LINHA};
        border-radius: 10px;
        padding: 0.4rem 0.6rem;
    }}
    hr {{ border-color: {LINHA} !important; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Dados
@st.cache_data
def carregar_dados():
    vagas = pd.read_csv("dados/vagas.csv")
    requisitos = pd.read_csv("dados/requisitos.csv")
    return vagas, requisitos

vagas, requisitos = carregar_dados()

st.sidebar.markdown("### Filtros")

niveis = sorted(vagas["nivel"].dropna().unique().tolist())
nivel_sel = st.sidebar.multiselect("Senioridade", niveis, default=niveis)

cidades = sorted(vagas["cidade"].dropna().unique().tolist())
cidade_sel = st.sidebar.multiselect("Localização", cidades, default=cidades)

vagas_f = vagas[vagas["nivel"].isin(nivel_sel) & vagas["cidade"].isin(cidade_sel)]

st.title("Mercado de Dados e BI em Portugal")
st.markdown(
    '<div class="sub">Competências pedidas, senioridade e localização das vagas '
    "recolhidas no LinkedIn.</div>",
    unsafe_allow_html=True,
)

if vagas_f.empty:
    st.warning("Nenhuma vaga corresponde aos filtros escolhidos.")
    st.stop()

req_f = pd.merge(vagas_f, requisitos, on="id_vaga")
req_validos = req_f[req_f["requisito"] != "Não especificado no anúncio"]


# KPIs
def kpi(label, valor, sub=""):
    return (
        f'<div class="kpi"><div class="kpi-label">{html.escape(label)}</div>'
        f'<div class="kpi-value">{html.escape(str(valor))}</div>'
        f'<div class="kpi-sub">{html.escape(sub)}</div></div>'
    )


total = len(vagas_f)
hibridas = int((vagas_f["modelo"] == "Híbrido").sum())

if req_validos.empty:
    top_nome, top_sub = "—", ""
else:
    contagem = req_validos["requisito"].value_counts()
    top_nome, top_sub = contagem.idxmax(), f"em {contagem.max()} vagas"

c1, c2, c3 = st.columns(3)
c1.markdown(kpi("Vagas selecionadas", total), unsafe_allow_html=True)
c2.markdown(kpi("Competência mais pedida", top_nome, top_sub), unsafe_allow_html=True)
c3.markdown(
    kpi("Modelo híbrido", f"{hibridas / total * 100:.0f}%", f"{hibridas} de {total} vagas"),
    unsafe_allow_html=True,
)

st.write("")

# Gráficos
def barras_horizontais(df, categoria, valor, altura=380):
    """Barras horizontais com a maior destacada e as restantes mais suaves."""
    df = df.sort_values(valor)
    cores = [DESTAQUE_SUAVE] * len(df)
    cores[-1] = DESTAQUE

    fig = go.Figure(
        go.Bar(
            x=df[valor],
            y=df[categoria],
            orientation="h",
            marker_color=cores,
            text=df[valor],
            textposition="outside",
            cliponaxis=False,
            hovertemplate="%{y}: %{x} vagas<extra></extra>",
        )
    )
    fig.update_layout(
        height=altura,
        margin=dict(l=0, r=30, t=10, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", color=TINTA, size=13),
        xaxis=dict(showgrid=True, gridcolor=LINHA, zeroline=False, title="", showticklabels=False),
        yaxis=dict(title="", showgrid=False),
        bargap=0.35,
    )
    return fig


CONFIG = {"displayModeBar": False}

esq, dir_ = st.columns([3, 2], gap="large")

with esq:
    st.markdown("### Competências mais pedidas")
    if req_validos.empty:
        st.info("Sem requisitos detalhados para os filtros atuais.")
    else:
        top = req_validos["requisito"].value_counts().head(10).reset_index()
        top.columns = ["Competência", "Vagas"]
        st.plotly_chart(barras_horizontais(top, "Competência", "Vagas"), use_container_width=True, config=CONFIG)

with dir_:
    st.markdown("### Vagas por cidade")
    cid = vagas_f["cidade"].value_counts().head(8).reset_index()
    cid.columns = ["Cidade", "Vagas"]
    st.plotly_chart(barras_horizontais(cid, "Cidade", "Vagas"), use_container_width=True, config=CONFIG)

st.write("")
st.markdown("### Senioridade e modelo de trabalho")
cruzado = vagas_f.groupby(["nivel", "modelo"]).size().reset_index(name="Vagas")
fig_nm = px.bar(
    cruzado,
    x="Vagas",
    y="nivel",
    color="modelo",
    orientation="h",
    color_discrete_sequence=[DESTAQUE, DESTAQUE_SUAVE, "#CBBFA9", "#8A8F98"],
    labels={"nivel": "", "modelo": ""},
)
fig_nm.update_layout(
    height=260,
    margin=dict(l=0, r=10, t=10, b=10),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter, sans-serif", color=TINTA, size=13),
    legend=dict(orientation="h", y=1.15, x=0, title=""),
    xaxis=dict(gridcolor=LINHA, zeroline=False, title=""),
    yaxis=dict(title=""),
    bargap=0.4,
)
st.plotly_chart(fig_nm, use_container_width=True, config=CONFIG)

# Tabela
st.divider()
st.markdown("### Lista de vagas")
tabela = vagas_f.rename(columns=lambda c: c.replace("_", " ").capitalize())
st.dataframe(tabela, use_container_width=True, hide_index=True)
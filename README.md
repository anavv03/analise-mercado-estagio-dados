# Análise do Mercado de Dados em Portugal — Guia para o Primeiro Estágio

Análise exploratória e dashboard interativo sobre os **requisitos técnicos, níveis de senioridade e distribuição geográfica** das ofertas de emprego na área de Dados em Portugal, com foco em orientar recém-licenciados na preparação para o primeiro estágio.


---

## Objetivo

Como recém-licenciada em Engenharia Informática à procura da primeira oportunidade na área de Dados, desenvolvi este projeto de ponta a ponta para responder, com dados reais, a uma pergunta prática:

**Quais são as competências mais exigidas pelo mercado português e como variam consoante o nível de experiência?**

---

## 🗂️ Recolha e Modelação dos Dados

Os dados foram recolhidos manualmente a partir de anúncios reais no LinkedIn em Portugal ([MÊS/ANO DA RECOLHA]). Na etapa de limpeza (*data cleaning*) foram removidas vagas duplicadas e anúncios fora do âmbito de Dados/BI, resultando numa base final de **25 vagas únicas**.

Para evitar redundância e facilitar cruzamentos, os dados estão num modelo relacional (`1:N`):

| Ficheiro | Descrição |
|---|---|
| `dados/vagas.csv` | Tabela principal com os metadados de cada vaga: `id_vaga`, `cargo`, `nivel`, `modelo`, `cidade` |
| `dados/requisitos.csv` | Competências padronizadas e categorizadas, ligadas à vaga através de `id_vaga` |

---

## Principais Descobertas

- **O trio fundamental:** SQL e Power BI lideram os requisitos técnicos (56% das vagas), seguidos do Excel (40%).
- **Estágio/Júnior vs. Sénior:** nas vagas de entrada (`Estágio/Trainee` e `Júnior`), a combinação **SQL + Power BI + Excel + Inglês** forma a base exigida. Python e plataformas Cloud (GCP/AWS) aparecem sobretudo em `Pleno/Sénior` e em Engenharia de Dados.
- **Concentração geográfica:** Lisboa e Porto concentram a grande maioria das oportunidades.
- **Transparência nos modelos de trabalho:** mais de metade dos anúncios não especifica o regime (remoto/híbrido/presencial) na descrição inicial.

---

## ⚠️ Limitações

- A amostra é pequena (25 vagas) e foi recolhida manualmente numa única plataforma, por isso os resultados são **indicativos e não representam todo o mercado**.
- As percentagens refletem o momento da recolha e podem variar com uma amostra maior.

---

## 🛠️ Tecnologias

- **Python (`pandas`)**: limpeza, tratamento e cruzamento relacional (`merge`) das tabelas
- **Streamlit e Plotly**: interface web interativa, cartões de KPI e gráficos dinâmicos
- **Git e GitHub**: controlo de versões e documentação

---

## Como Executar Localmente

1. Clonar o repositório:

```bash
git clone https://github.com/anavv03/analise-mercado-estagio-dados.git
cd analise-mercado-estagio-dados
```

2. (Recomendado) Criar e ativar um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

3. Instalar as dependências:

```bash
pip install -r requirements.txt
```

4. Executar o dashboard:

```bash
streamlit run [NOME_DO_FICHEIRO].py
```

O dashboard abre em `http://localhost:8501`.

---

## 📁 Estrutura do Projeto

```
analise-mercado-estagio-dados/
├── dados/
│   ├── vagas.csv
│   └── requisitos.csv
├── [NOME_DO_FICHEIRO].py
├── requirements.txt
└── README.md
```

---

## Próximos Passos

- Aumentar a amostra e incluir mais fontes de anúncios
- Acompanhar a evolução das competências ao longo do tempo
- Automatizar a recolha de dados

---

## Autora

**Ana Venâncio** 
[GitHub: @anavv03](https://github.com/anavv03)

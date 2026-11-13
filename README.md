# Mercado de Dados e BI em Portugal

Análise exploratória e dashboard interativo sobre os requisitos técnicos, níveis de senioridade e distribuição geográfica das ofertas de emprego na área de Dados em Portugal, com foco em orientar recém-licenciados na preparação para o primeiro estágio.

## Objetivo do Projeto
Como recém-licenciado à procura da primeira oportunidade na área de Dados, desenvolvi este projeto de ponta a ponta para responder com dados reais a uma pergunta prática: **quais são as competências mais exigidas pelo mercado português e como variam consoante o nível de experiência?**

## 🗂️ Recolha e Modelação dos Dados
Os dados foram recolhidos manualmente a partir de anúncios reais no LinkedIn em Portugal. Durante a etapa de limpeza (*Data Cleaning*), foram removidas vagas duplicadas e anúncios fora do escopo de Dados/BI, resultando numa base final de **25 vagas únicas**.

Para evitar redundância e facilitar cruzamentos analíticos, os dados foram estruturados num **modelo relacional (`1:N`)**:
* **`dados/vagas.csv`**: Tabela principal com os metadados de cada oportunidade (`id_vaga`, `cargo`, `nivel`, `modelo`, `cidade`).
* **`dados/requisitos.csv`**: Tabela de competências padronizadas e categorizadas, relacionada através da chave `id_vaga`.

## Principais Descobertas (Insights)
* **O trio fundamental:** **SQL** e **Power BI** lideram os requisitos técnicos (presentes em 56% das vagas analisadas), seguidos pelo **Excel** (40%).
* **Perfil Estágio & Júnior vs. Sénior:** Nas vagas de entrada (`Estágio/Trainee` e `Júnior`), a combinação de **SQL + Power BI + Excel** (aliada ao **Inglês**) forma a base exigida. Ferramentas como **Python** e plataformas **Cloud (GCP/AWS)** surgem maioritariamente quando a senioridade sobe para `Pleno/Sénior` ou Engenharia de Dados.
* **Concentração Geográfica:** **Lisboa** e **Porto** concentram a grande maioria das oportunidades no país.
* **Transparência nos Modelos de Trabalho:** Mais de metade dos anúncios analisados não especifica o regime (remoto/híbrido/presencial) de forma explícita na descrição inicial.

##  Tecnologias Utilizadas
* **Python (`pandas`):** Limpeza, tratamento e cruzamento relacional (`merge`) das tabelas.
* **Streamlit & Plotly:** Desenvolvimento da interface web interativa, cartões de KPI e visualizações dinâmicas.
* **Git & GitHub:** Controlo de versões e documentação.

##  Como Executar Localmente

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/anavv03/analise-mercado-estagio-dados.git]
   (https://github.com/anavv03/analise-mercado-estagio-dados.git)
   cd analise-mercado-estagio-dados
import pandas as pd
import matplotlib.pyplot as plt

#Carrega as tabelas relacionais
vagas = pd.read_csv("dados/vagas.csv")
requisitos = pd.read_csv("dados/requisitos.csv")

print(f"Total de vagas analisadas: {len(vagas)}")

#Top 10 Requisitos mais exigidos
req_validos = requisitos[requisitos["requisito"] != "Não especificado no anúncio"]
top_requisitos = req_validos["requisito"].value_counts().head(10)

print("\n--- TOP 10 REQUISITOS ---")
print(top_requisitos)

#Dados para encontrar os requisitos mais pedidos apenas para Estágio/Trainee e Júnior
df_completo = pd.merge(vagas, req_validos, on="id_vaga")
iniciantes = df_completo[df_completo["nivel"].isin(["Estágio/Trainee", "Júnior"])]
top_iniciantes = iniciantes["requisito"].value_counts().head(8)

print("\n--- TOP REQUISITOS (ESTÁGIO & JÚNIOR) ---")
print(top_iniciantes)

#Gerar o Gráfico de Ranking Geral de Competências
plt.figure(figsize=(10, 6))
top_requisitos.sort_values().plot(kind="barh", color="#2b5c8f")
plt.title("Top 10 Competências Mais Exigidas em Dados (Portugal)", fontsize=13, fontweight="bold")
plt.xlabel("Número de Vagas")
plt.ylabel("")
plt.grid(axis="x", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("grafico_top_requisitos.png", dpi=300)
plt.close()

#Gráfico de Distribuição por Nível e Cidade
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

vagas["nivel"].value_counts().plot(kind="bar", ax=axes[0], color="#3b82f6", rot=0)
axes[0].set_title("Vagas por Nível de Senioridade", fontweight="bold")
axes[0].set_ylabel("Quantidade")

vagas["cidade"].value_counts().head(5).plot(kind="bar", ax=axes[1], color="#10b981", rot=15)
axes[1].set_title("Distribuição Geográfica", fontweight="bold")

plt.tight_layout()
plt.savefig("grafico_distribuicao.png", dpi=300)
plt.close()

print("\nGráficos guardados com sucesso: 'grafico_top_requisitos.png' e 'grafico_distribuicao.png'")
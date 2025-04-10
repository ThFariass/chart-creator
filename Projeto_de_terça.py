#LINK SHEETS 1t6IenPo-hUzwVv2_dEfTuI-1JVsa1Q1cdWJbrWblH4k

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Autenticação com a API do Google
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json", scope)
client = gspread.authorize(creds)

# Abrir a planilha pelo ID
spreadsheet_id = "18Cg3p1NfAIS7GSxdoVYZhrWAMIvVggIrtaEp_R9XU4E"
sheet = client.open_by_key(spreadsheet_id).sheet1

# 3. Carregar dados em um DataFrame
data = sheet.get_all_records()
df = pd.DataFrame(data)

# 4. Limpar colunas (remover espaços)
df.columns = [
    "entity", "code", "year",
    "schizophrenia", "depressive", "anxiety",
    "bipolar", "eating"
]

df["year"] = df["year"].astype(int)

# Define anos
ano_inicial = df["year"].min()
ano_final = df["year"].max()

# Seleciona as 6 cidades com maior média de distúrbios no ano final
top_cidades = (
    df[df["year"] == ano_final]
    .groupby("entity")[["schizophrenia", "depressive", "anxiety", "bipolar", "eating"]]
    .mean()
    .mean(axis=1)
    .sort_values(ascending=False)
    .head(6)
    .index.tolist()
)

df_filtrado = df[df["entity"].isin(top_cidades)]

# === GRÁFICO DE LINHAS: Evolução dos distúrbios nas 6 principais cidades ===
disturbios = ["schizophrenia", "depressive", "anxiety", "bipolar", "eating"]
for dist in disturbios:
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df_filtrado, x="year", y=dist, hue="entity", marker="o")
    plt.title(f"Evolução da taxa de {dist.capitalize()} – Top Cidades")
    plt.xlabel("Ano")
    plt.ylabel("Taxa (%)")
    plt.legend(title="Cidade")
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.tight_layout()
    plt.show()

# === GRÁFICO DE BARRAS: Comparação de cada distúrbio no primeiro vs. último ano ===
df_inicio = df[(df["year"] == ano_inicial) & (df["entity"].isin(top_cidades))]
df_fim = df[(df["year"] == ano_final) & (df["entity"].isin(top_cidades))]

for dist in disturbios:
    df_bar = pd.DataFrame({
        "Cidade": top_cidades,
        f"{ano_inicial}": df_inicio.set_index("entity")[dist],
        f"{ano_final}": df_fim.set_index("entity")[dist]
    }).reset_index(drop=True)

    df_bar_melted = df_bar.melt(id_vars="Cidade", var_name="Ano", value_name="Taxa")

    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_bar_melted, x="Cidade", y="Taxa", hue="Ano")
    plt.title(f"Comparação da taxa de {dist.capitalize()} ({ano_inicial} vs {ano_final})")
    plt.ylabel("Taxa (%)")
    plt.xlabel("Cidade")
    plt.legend(title="Ano")
    plt.tight_layout()
    plt.show()




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
spreadsheet_id = "1LCo051AtXvsEV17rL_7Vgw7HJXUu7kaa7_7a1eFMl-I"
sheet = client.open_by_key(spreadsheet_id).sheet1

# 3. Carregar dados em um DataFrame
data = sheet.get_all_records()
df = pd.DataFrame(data)

# 4. Limpar colunas (remover espaços)
df.columns = df.columns.str.strip()

print("Colunas disponíveis:", df.columns.tolist())
print("Quantidade de linhas:", len(df))
print("Amostra dos dados:")
print(df.head())

# Verificar visualmente as colunas e as 5 primeiras linhas
print("Colunas no DataFrame:")
print(df.columns.tolist())
print("\nAmostra dos dados:")
print(df.head())


# Gráfico 1: Média de calorias por gênero
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x="Gender", y="Calories_Intake", estimator="mean")
plt.title("Média de Calorias Ingeridas por Gênero")
plt.ylabel("Calorias (média)")
plt.xlabel("Gênero")
plt.show()

# Gráfico 2: Altura vs Peso com distinção de gênero
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="Height_cm", y="Weight_kg", hue="Gender")
plt.title("Altura vs Peso por Gênero")
plt.xlabel("Altura (cm)")
plt.ylabel("Peso (kg)")
plt.show()

# Gráfico 3: Boxplot de horas de sono por diabéticos
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x="Diabetic", y="Hours_of_Sleep")
plt.title("Horas de Sono por Condição Diabética")
plt.xlabel("É Diabético?")
plt.ylabel("Horas de Sono")
plt.show()

# Gráfico 4: Distribuição de doença cardíaca
plt.figure(figsize=(6, 5))
sns.countplot(data=df, x="Heart_Disease")
plt.title("Distribuição de Pessoas com Doença Cardíaca")
plt.xlabel("Doença Cardíaca")
plt.ylabel("Número de Pessoas")
plt.show()

print("Quantidade de linhas:", len(df))

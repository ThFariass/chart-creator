**Mental Health Analytics com Google Sheets & Python Projeto de visualização de dados de saúde mental, utilizando Python, Google Sheets API e bibliotecas de visualização como matplotlib e seaborn.**

**Funcionalidades**
Integração com Google Sheets para carregar datasets.

Geração de gráficos profissionais e limpos sobre distúrbios mentais por cidade e por ano.

Comparações entre o primeiro e o último ano dos dados.

Foco em 6 cidades por vez para uma visualização clara e objetiva.

**Como executar o projeto**
**1. Clone o repositório**
bash
Copiar
Editar
git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo
**2. Instale as dependências**
Você pode usar pip ou um ambiente como Anaconda:

bash
Copiar
Editar
pip install pandas seaborn matplotlib gspread oauth2client
**3. Configure a API do Google Sheets
3.1. Acesse o Google Cloud Console**
Acesse https://console.cloud.google.com/

Crie um novo projeto.

Vá para "APIs e Serviços" > "Tela de consentimento OAuth" e configure como "externo" (pode ser teste).

Vá para "Credenciais" e crie um novo:

Tipo: Conta de Serviço

Selecione o projeto

Clique em "Criar chave" > JSON

**3.2. Baixe a chave JSON**
Renomeie o arquivo para credenciais.json e coloque na raiz do projeto.

**3.3. Compartilhe sua planilha**
Abra seu Google Sheets, clique em "Compartilhar" e adicione o e-mail da conta de serviço (algo como xxx@xxx.iam.gserviceaccount.com) com permissão de Leitura.

**4. Execute o script
Você pode carregar os dados direto da planilha ou usar um .csv. Para carregar do Sheets:**

python
Copiar
Editar
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json", scope)
client = gspread.authorize(creds)

spreadsheet = client.open_by_key("SEU_ID_DA_PLANILHA")
sheet = spreadsheet.sheet1
data = sheet.get_all_records()

df = pd.DataFrame(data)
Ou simplesmente carregue um CSV salvo localmente:

python
Copiar
Editar
df = pd.read_csv("disturbios_mentais.csv")
📈 Sobre os gráficos
O script principal faz:

Filtragem automática das 6 cidades mais afetadas

Gera:

Gráficos de linha por distúrbio, mostrando a evolução por cidade ao longo dos anos.

Gráficos de barras comparando o primeiro e o último ano de cada distúrbio.

Visual limpo e responsivo, com uso de seaborn e matplotlib.

**Colunas esperadas no dataset**
Coluna	Descrição
Entity	Nome da cidade ou país
Code	Código da entidade
Year	Ano da medição
Schizophrenia	Taxa de esquizofrenia (%)
Depressive	Taxa de depressão (%)
Anxiety	Taxa de ansiedade (%)
Bipolar	Taxa de transtorno bipolar (%)
Eating	Taxa de transtorno alimentar (%)
**Estrutura recomendada**
bash
Copiar
Editar
mental-health-analytics/
│
├── credenciais.json         # Sua chave da API do Google
├── disturbios_mentais.csv   # Dataset (caso não use Google Sheets)
├── graficos.py              # Script principal
├── README.md                # Documentação do projeto
└── requirements.txt         # Dependências (opcional)
**Observações**
O projeto foi desenvolvido para uso acadêmico e visualização exploratória.

Você pode adaptar os gráficos para exibir apenas cidades específicas, períodos de tempo, ou até aplicar filtros geográficos.

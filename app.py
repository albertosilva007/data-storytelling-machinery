# app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configurações iniciais da página
st.set_page_config(page_title="Análise de Máquinas", page_icon="🛠️", layout="wide")

# Função para carregar os dados
@st.cache_data
def load_data():
    return pd.read_csv('machinery_data.csv')

# Carregar os dados
df = load_data()

# Título
st.title("🛠️ Análise de Dados de Máquinas Industriais")

# Descrição inicial
st.markdown("""
Este dashboard explora o desempenho de diferentes tipos de máquinas, buscando entender o impacto das **horas de uso** e **temperaturas** em **falhas** e **manutenção**.
""")

# Seção: Visão geral dos dados
st.header("🔎 Visão Geral dos Dados")
st.dataframe(df)

# Seção: Tipos de máquina
st.header("🏗️ Quantidade de Máquinas por Tipo")

fig1, ax1 = plt.subplots()
sns.countplot(data=df, x='Machine_Type', palette="viridis", ax=ax1)
ax1.set_xlabel("Tipo de Máquina")
ax1.set_ylabel("Quantidade")
ax1.set_title("Distribuição de Máquinas por Tipo")
st.pyplot(fig1)

# Seção: Uso vs Temperatura
st.header("🌡️ Relação entre Uso e Temperatura")

fig2, ax2 = plt.subplots()
sns.scatterplot(data=df, x='Usage_Hours', y='Temperature', hue='Machine_Type', palette="coolwarm", ax=ax2)
ax2.set_xlabel("Horas de Uso")
ax2.set_ylabel("Temperatura (°C)")
ax2.set_title("Horas de Uso vs Temperatura")
st.pyplot(fig2)

# Seção: Análise de Falhas
st.header("🚨 Máquinas que Apresentaram Falhas")

failures = df[df['Failures'] > 0]
if not failures.empty:
    st.dataframe(failures)
else:
    st.success("Nenhuma falha detectada! ✅")

# Insights finais
st.header("💡 Insights e Recomendações")

st.markdown("""
- Monitorar máquinas que operam acima de **60°C**, pois podem apresentar riscos maiores de falha.
- Implementar **manutenções preventivas** após **100 horas** de uso contínuo.
- Priorizar manutenção em máquinas do tipo **Lathe** e **Milling**, que operam em faixas de temperatura mais elevadas.
""")

# Rodapé
st.markdown("---")
st.caption("Desenvolvido para o desafio de Data Storytelling 🚀")

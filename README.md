# 🏥 HealthCare Data Analysis – Projeto de Ciência de Dados

Este projeto foi desenvolvido como parte da avaliação prática da disciplina de **Ciência de Dados Aplicada à Saúde**, com o objetivo de propor uma solução analítica para melhorar o atendimento hospitalar e a jornada do paciente através de decisões orientadas por dados.

---

## 📘 Parte 1 – Relatório Teórico

O relatório em PDF (`relatorio_teorico.pdf`) apresenta:

### 🔹 Cenário-Problema
A **HealthCare Solutions** enfrenta dificuldades em identificar padrões de readmissão e satisfação dos pacientes. A análise de dados foi utilizada para compreender os principais fatores que influenciam a qualidade do atendimento e propor melhorias baseadas em evidências.

### 🔹 Fontes de Dados
- Registros eletrônicos de saúde (EHR)
- Dispositivos de monitoramento (wearables)
- Pesquisas de satisfação dos pacientes
- Dados administrativos e operacionais

### 🔹 Fundamentos da Ciência de Dados
O projeto segue todas as etapas de um processo completo:
1. **Coleta de dados**
2. **Limpeza e pré-processamento**
3. **Análise exploratória (EDA)**
4. **Modelagem preditiva**
5. **Visualização e interpretação dos resultados**

### 🔹 Ética e LGPD
Foi considerado o uso responsável de dados sensíveis de saúde, respeitando os princípios da **LGPD**, como anonimização, consentimento e transparência no tratamento das informações.

### 🔹 Levantamento de Requisitos
Foram elaboradas **10 perguntas simuladas** à equipe de gestão da empresa, com respostas que guiaram o foco analítico (ex: identificar fatores que aumentam o tempo médio de internação).

---

## 💻 Parte 2 – Projeto Prático em Python

O arquivo `pratica_healthcare.py` contém um pipeline completo de análise de dados hospitalares.

### 🧩 Tecnologias Utilizadas
- **Python 3.13**
- **Bibliotecas:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`
- **IDE recomendada:** Jupyter Notebook ou VSCode
- **Visualizações:** Matplotlib e Seaborn

### ⚙️ Etapas do Projeto

#### 1. Coleta de Dados
Os dados foram simulados em CSV com informações anonimizadas de pacientes, como idade, pressão arterial, nível de glicose, tempo de internação e satisfação.

#### 2. Limpeza e Pré-Processamento
- Remoção de duplicatas  
- Tratamento de valores ausentes  
- Padronização das colunas numéricas e categóricas  

#### 3. Análise Exploratória (EDA)
Foram criados:
- Histogramas de distribuição  
- Gráficos de dispersão  
- Heatmap de correlação  

#### 4. Modelagem Preditiva
Aplicou-se o algoritmo **Random Forest Classifier** para prever o **risco de readmissão** hospitalar.  
O modelo foi avaliado com **acurácia, precisão e recall**.

#### 5. Visualização de Resultados
Os principais insights foram destacados em gráficos e prints no PDF, mostrando:
- Fatores que mais influenciam o risco de readmissão  
- Relação entre satisfação e tempo de internação  

---

## 🧠 Principais Insights
- Pacientes com maior tempo de internação apresentam maior chance de readmissão.  
- A idade e o nível de glicose foram variáveis fortemente correlacionadas ao risco.  
- A Random Forest obteve alta performance, sendo útil para prever casos de risco.

---
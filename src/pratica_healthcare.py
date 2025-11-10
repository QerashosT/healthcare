import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, auc
import os

# --- CONFIGURAÇÃO ---
os.makedirs('outputs', exist_ok=True)
np.random.seed(42)

# --- COLETA DE DADOS (Simulação) ---
n = 400
dados = pd.DataFrame({
    'idade': np.random.randint(20, 90, n),
    'sexo': np.random.choice(['M', 'F'], n),
    'dias_internacao': np.random.randint(1, 15, n),
    'pressao': np.random.randint(90, 160, n),
    'frequencia_cardiaca': np.random.randint(60, 120, n),
    'satisfacao': np.random.randint(1, 6, n),
    'tempo_espera_horas': np.random.uniform(0.5, 8, n),
    'comorbidades': np.random.randint(0, 5, n)
})
dados['readmissao_30d'] = np.where(
    (dados['idade'] > 60) & (dados['comorbidades'] >= 2) & (dados['satisfacao'] <= 2), 1, 0
)
dados.to_csv('data/dataset_simulado.csv', index=False)

# --- LIMPEZA ---
dados.drop_duplicates(inplace=True)
dados.fillna(dados.mean(numeric_only=True), inplace=True)

# --- ANÁLISE EXPLORATÓRIA (EDA) ---
plt.figure(figsize=(8,5))
sns.countplot(x='readmissao_30d', data=dados)
plt.title('Distribuição de Readmissões em 30 dias')
plt.savefig('outputs/readmission_count.png')
plt.close()

plt.figure(figsize=(8,5))
sns.boxplot(x='readmissao_30d', y='idade', data=dados)
plt.title('Idade vs Readmissão')
plt.savefig('outputs/age_vs_readmission.png')
plt.close()

plt.figure(figsize=(8,6))
sns.heatmap(dados.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlação entre Variáveis')
plt.savefig('outputs/correlation_heatmap.png')
plt.close()

# --- MODELAGEM PREDITIVA ---
dados = pd.get_dummies(dados, columns=['sexo'], drop_first=True)
X = dados.drop('readmissao_30d', axis=1)
y = dados['readmissao_30d']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

modelos = {
    'Regressão Logística': LogisticRegression(max_iter=1000),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42)
}

resultados = {}
for nome, modelo in modelos.items():
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    resultados[nome] = acc

melhor_modelo_nome = max(resultados, key=resultados.get)
melhor_modelo = modelos[melhor_modelo_nome]
print(f"Melhor modelo: {melhor_modelo_nome} (Acurácia: {resultados[melhor_modelo_nome]:.2f})")

# --- RELATÓRIO DE DESEMPENHO ---
y_pred = melhor_modelo.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Matriz de Confusão')
plt.savefig('outputs/confusion_matrix.png')
plt.close()

print(classification_report(y_test, y_pred))

# --- CURVA ROC ---
y_prob = melhor_modelo.predict_proba(X_test)[:,1]
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(6,5))
plt.plot(fpr, tpr, label=f'ROC Curve (AUC = {roc_auc:.2f})')
plt.plot([0,1],[0,1],'--',color='gray')
plt.xlabel('Falsos Positivos')
plt.ylabel('Verdadeiros Positivos')
plt.title('Curva ROC')
plt.legend()
plt.savefig('outputs/roc_curve.png')
plt.close()

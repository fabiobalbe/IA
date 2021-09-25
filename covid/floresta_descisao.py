import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

dataset = pd.read_excel("dataset-covid_einstein-TRATADO.xlsx")
colunas = dataset.columns.tolist()
colunasTratadas = colunas[2:3] + colunas[4:]

x = dataset[colunasTratadas]
y = dataset.iloc[:, 3].values

x_treino, x_teste, y_treino, y_teste = train_test_split(
    x, y, test_size=0.25, random_state=0
)

florestaRandomica = RandomForestClassifier(n_estimators=10)

florestaRandomica.fit(x_treino, y_treino)

resultado = florestaRandomica.predict(x_teste)

print("Acurácia:", metrics.accuracy_score(y_teste, resultado))

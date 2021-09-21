import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

dataset = pd.read_excel("dataset-covid_einstein-TRATADO.xlsx")

x = dataset.iloc[:, 4:].values  # TEM QUE ADD COLUNA DA IDADE PARA FICAR MAIS COMPLETO
y = dataset.iloc[:, 3].values

x_treino, x_teste, y_treino, y_teste = train_test_split(
    x, y, test_size=0.25, random_state=0
)

arvore = DecisionTreeClassifier()
arvore = arvore.fit(x_treino, y_treino)

resultado = arvore.predict(x_teste)

print(metrics.classification_report(y_teste, resultado))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB

dataset = pd.read_excel("dataset-covid_einstein-TRATADO.xlsx")

x = dataset.iloc[:, 4:].values  # TEM QUE ADD COLUNA DA IDADE PARA FICAR MAIS COMPLETO
y = dataset.iloc[:, 3].values

x_treino, x_teste, y_treino, y_teste = train_test_split(
    x, y, test_size=0.25, random_state=0
)
gauss = GaussianNB()

gauss.fit(x_treino, y_treino)

resultados_gauss = gauss.predict(x_teste)

print("Acurácia: ", metrics.accuracy_score(y_teste, resultados_gauss))

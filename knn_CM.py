import pandas as pd  # importando o módulo pandas para tratar os dados
from sklearn.model_selection import (
    train_test_split,
)  # importa o módulo sklearn - aprendizado de máquina
from sklearn.preprocessing import StandardScaler  # normalizador de dados
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd
from sklearn.svm import SVC

dataset = pd.read_csv("bc_data2.csv")
dataset["Unnamed: 32"] = dataset["Unnamed: 32"].fillna(0)
dataset.head(2)

x = dataset.iloc[:, 2:].values
y = dataset.iloc[:, 1].values

x_treino, x_teste, y_treino, y_teste = train_test_split(
    x, y, test_size=0.25, random_state=0
)

normalizador = StandardScaler()
x_treino = normalizador.fit_transform(x_treino)
x_teste = normalizador.fit_transform(x_teste)

print(x_treino.shape)
print(x_teste.shape)

classificador = KNeighborsClassifier(n_neighbors=5, metric="manhattan", p=2)

classificador = classificador.fit(x_treino, y_treino)

preditor = classificador.predict(x_teste)
acuracia = metrics.accuracy_score(y_teste, preditor)

print("Acurácia: {:.2f}".format(acuracia))

clf = SVC(random_state=0)
clf.fit(x_treino, y_treino)
plot_confusion_matrix(clf, x_teste, y_teste, display_labels=["Verdadeiro", "Falso"])
plt.show()


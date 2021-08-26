from ipywidgets.widgets.interaction import interactive
from numpy.core.fromnumeric import shape
from numpy.lib.function_base import gradient
from numpy.lib.shape_base import split
from numpy.lib.utils import source
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv("bc_data2.csv")
dataset["Unnamed: 32"] = dataset["Unnamed: 32"].fillna(0)

x = dataset.iloc[:, 2:].values
y = dataset.iloc[:, 1].values

x_treino, x_teste, y_treino, y_teste = train_test_split(
    x, y, test_size=0.25, random_state=0
)

normalizador = StandardScaler()
x_treino = normalizador.fit_transform(x_treino)
x_teste = normalizador.fit_transform(x_teste)

# CODIGO ARVORE DE DESCISÃO

from sklearn.tree import DecisionTreeClassifier

arvore = DecisionTreeClassifier()

# TREINANDO ARVORE DESCISÃO

arvore = arvore.fit(x_treino, y_treino)

print(arvore.feature_importances_)

for caracteristica, importancia in zip(dataset.columns, arvore.feature_importances_):
    print("{}: {}".format(caracteristica, importancia))

resultado = arvore.predict(x_teste)

# AVALIA SE A PREDIÇÃO DA ARVORE É CORRETA

from sklearn import metrics

print(metrics.classification_report(y_teste, resultado))

paciente = x_treino[45]

print(paciente)

diagnostico = arvore.predict([paciente])

print(diagnostico)

from ipywidgets import interactive
from IPython.display import SVG, display
from graphviz import Source

colunas = dataset.columns  # nome das colunas
classes = ["B", "M"]


def plot_tree(crit, split, depth, min_samples_split, min_samples_leaf=0.2):
    estimador = DecisionTreeClassifier(
        random_state=0,
        criterion=crit,
        splitter=min_samples_split,
        max_depth=depth,
        min_samples_leaf=min_samples_leaf,
    )
    estimador.fit(x_treino, y_treino)  # treinar
    graph = Source(
        export_graphviz(
            estimador,
            out_file=None,
            feature_names=colunas,
            class_names=classes,
            impurity=True,
            filled=True,
        )
    )
    display(SVG(graph.pipe(format="svg")))
    return estimador


inter = interactive(
    plot_tree,
    crit=["gini", "entropy"],
    split=["best", "random"],
    depth=[1, 2, 3, 4, 5, 6],
    min_samples_split=(1, 5),
    min_samples_leaf=(1, 5),
)
display(inter)


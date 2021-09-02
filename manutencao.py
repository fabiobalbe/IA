import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

dataset = pd.read_csv("ObesityDataSet_raw_and_data_sinthetic.csv")

encoder = OrdinalEncoder()

dataset["Gender"] = encoder.fit_transform(pd.DataFrame(dataset["Gender"]))
dataset["family_history_with_overweight"] = encoder.fit_transform(
    pd.DataFrame(dataset["family_history_with_overweight"])
)
dataset["FAVC"] = encoder.fit_transform(pd.DataFrame(dataset["FAVC"]))
dataset["CAEC"] = encoder.fit_transform(pd.DataFrame(dataset["CAEC"]))
dataset["SMOKE"] = encoder.fit_transform(pd.DataFrame(dataset["SMOKE"]))
dataset["SCC"] = encoder.fit_transform(pd.DataFrame(dataset["SCC"]))
dataset["CALC"] = encoder.fit_transform(pd.DataFrame(dataset["CALC"]))
dataset["MTRANS"] = encoder.fit_transform(pd.DataFrame(dataset["MTRANS"]))
dados = dataset.iloc[:, :16].values  # até a 16, não incluso a coluna 16
nomeclasses = dataset.iloc[:, 16].values  # somente a coluna 16

df = pd.DataFrame(nomeclasses)  # transformo o array em dataframe
classes = encoder.fit_transform(df)

# quebra o dataframe de teste e de treino a partir das variáveis x e y
x_treino, x_teste, y_treino, y_teste = train_test_split(
    dados, classes, test_size=0.25, random_state=5
)

# vamos codificar a árvore de decisão
arvore = DecisionTreeClassifier()

# treinando a árvore de decisão
arvore = arvore.fit(x_treino, y_treino)

for caracteristica, importancia in zip(dataset.columns, arvore.feature_importances_):
    print("{}:{}".format(caracteristica, importancia))


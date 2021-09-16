import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB

dataset = pd.read_csv("ObesityDataSet_raw_and_data_sinthetic.csv")
encoder = OrdinalEncoder()

# codificamos as colunas que não são numéricas para valores numéricos através do encoder
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
dataset["NObeyesdad"] = encoder.fit_transform(pd.DataFrame(dataset["NObeyesdad"]))

# separando os dados das classes do dataset
dados = dataset.iloc[:, :16].values  # até a 16, não incluso a coluna 16
nomeclasses = dataset.iloc[:, 16].values  # somente a coluna 16

# construindo a floresta randomica para classificar os dados por ML
# quebra o dataframe de teste e de treino a partir das variáveis x e y
x_treino, x_teste, y_treino, y_teste = train_test_split(
    dados, nomeclasses, test_size=0.25, random_state=5
)

# criar o classificador Gaussiano
gauss = GaussianNB()

# treinar o classificador
gauss.fit(x_treino, y_treino)

# resultados de predicao
resultados_gauss = gauss.predict(x_teste)

# avaliar a metrica de acerto do Gauss
print("Acurácia: ", metrics.accuracy_score(y_teste, resultados_gauss))

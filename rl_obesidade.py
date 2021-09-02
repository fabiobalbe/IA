import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import data
from sklearn.linear_model import LinearRegression as lr

dataset = pd.read_csv("ObesityDataSet_raw_and_data_sinthetic.csv")

plt.scatter(dataset["Height"], dataset["Weight"])
# plt.show()

# CALCULO DE IMC
def imc(massa, altura):
    return massa / (altura * altura)


# aplicar no dataset a função imc criando a columa IMC
dataset = dataset.assign(IMC=lambda x: imc(x["Weight"], x["Height"]))

dataset.head()

plt.scatter(dataset["Weight"], dataset["IMC"])
# plt.show()

ax, fig = plt.subplots()
fig.set_title("Relação peso x IMC")
plt.scatter(dataset["Weight"], dataset["IMC"], label="indivíduo")
fig.grid(True)
fig.set_xlabel("Peso")
fig.set_ylabel("IMC")
fig.legend()
# plt.show()

# regreção linear
pesos = dataset["Weight"].values.reshape(-1, 1)  # redesenha o array
valores_imc = dataset["IMC"].values.reshape(-1, 1)

funcao = lr()  # funcao que define a regreção linear

# treinar a função
funcao.fit(pesos, valores_imc)

# traçar os novos dados a partir da função que foi treinada acima
imc_esperados = funcao.predict(pesos)

# refazendo o grafico de pesos vs imc
ax, fig = plt.subplots()
fig.set_title("Relação peso x IMC")
plt.scatter(dataset["Weight"], dataset["IMC"], label="indivíduo")
plt.plot(dataset["Weight"], imc_esperados, label="Função de regreção", color="red")
fig.grid(True)
fig.set_xlabel("Peso")
fig.set_ylabel("IMC")
fig.legend()

# regreção linear ALTURA VS IMC
alturas = dataset["Height"].values.reshape(-1, 1)  # redesenha o array

funcao.fit(alturas, valores_imc)  # treinar a função

# traçar os novos dados a partir da função que foi treinada acima
imc_esperados = funcao.predict(alturas)

# refazendo o grafico de pepsos vs imc
ax, fig = plt.subplots()
fig.set_title("Relação altura x IMC")
plt.scatter(dataset["Height"], dataset["IMC"], label="indivíduo")
plt.plot(dataset["Height"], imc_esperados, label="Função de regressão", color="red")
fig.grid(True)
fig.set_xlabel("Altura")
fig.set_ylabel("IMC")
fig.legend()
plt.show()
# agrupando os individuos do dataset conforme um critério estabelecido
menores = dataset.loc[dataset["Age"] < 18]
menores.info()
plt.scatter(menores["Weight"], menores["IMC"])
plt.show()

maiores = dataset.loc[dataset["Age"] > 18]
maiores.info()
plt.scatter(maiores["Weight"], maiores["IMC"])
plt.show()

# maiores fumantes
maiores_fumantes = maiores.loc[maiores["SMOKE"] == "yes"]
alturas = maiores_fumantes["Height"].values.reshape(-1, 1)
valores_imc = maiores_fumantes["IMC"].values.reshape(-1, 1)
funcao.fit(alturas, valores_imc)
imc_esperados = funcao.predict(alturas)
ax, fig = plt.subplots()
fig.set_title("Relação altura x IMC -- FUMANTES")
plt.scatter(maiores_fumantes["Height"], maiores_fumantes["IMC"], label="indivíduo")
plt.plot(
    maiores_fumantes["Height"], imc_esperados, label="Função de regressão", color="red"
)
fig.grid(True)
fig.set_xlabel("Altura")
fig.set_ylabel("IMC")
fig.legend()
plt.show()

# grafico que mostre relação peso X imc para quem tem imc > 25
# relacionando o idade com a altura

obesos = dataset.loc[dataset["IMC"] > 25]
ax, fig = plt.subplots()
fig.set_title("Relação idade x altura -- OBESOS")
plt.scatter(obesos["Age"], obesos["Height"], label="indivíduo")
fig.grid(True)
fig.set_xlabel("Idade")
fig.set_ylabel("Altura")
fig.legend()
plt.show()


# regreção linear Idade VS altura
alturas = obesos["Height"].values.reshape(-1, 1)  # redesenha o array
idades = obesos["Age"].values.reshape(-1, 1)  # redesenha o array
funcao.fit(idades, alturas)  # treinar a função

# traçar os novos dados a partir da função que foi treinada acima
idades_esperadas = funcao.predict(idades)


ax, fig = plt.subplots()
fig.set_title("Relação idade x altura -- OBESOS")
plt.scatter(obesos["Age"], obesos["Height"], label="indivíduo")
plt.plot(obesos["Age"], idades_esperadas, label="Função de regressão", color="blue")
fig.grid(True)
fig.set_xlabel("Idade")
fig.set_ylabel("Altura")
fig.legend()
plt.show()

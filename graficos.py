import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("ObesityDataSet_raw_and_data_sinthetic.csv")

print(dataset.head())

# Pessoas que consomem alimentos com alta caloria
altaCaloria = dataset.loc[dataset["FAVC"] == "yes"]
print(altaCaloria.head())


def imc(massa, altura):
    return massa / (altura * altura)


plt.scatter(baixaCaloria["Height"], baixaCaloria["Weight"])
plt.show()


altaCaloria = altaCaloria.assign(IMC=lambda x: imc(x["Weight"], x["Height"]))

altaCaloria = altaCaloria.assign(IMC=lambda x: imc(x["Weight"], x["Height"]))

ax, fig = plt.subplots()
fig.set_title("Relação peso x IMC")
plt.scatter(altaCaloria["Weight"], altaCaloria["IMC"], label="indivíduo")
fig.grid(True)
fig.set_xlabel("Peso")
fig.set_ylabel("IMC")
fig.legend()
plt.show()

baixaCaloria = dataset.loc[dataset["FAVC" == "no"]]


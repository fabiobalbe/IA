import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

dataset = pd.read_excel("dataset-covid_einstein.xlsx")

dataset = dataset.fillna(0)
print(dataset["CoronavirusNL63"])
encoder = OrdinalEncoder()

dataset["CoronavirusNL63"] = encoder.fit_transform(
    pd.DataFrame(dataset["CoronavirusNL63"])
)

print(dataset["CoronavirusNL63"])

# NEM TODAS AS LINHAS COM STRING ESTÃO PREENCHIDAS, PORTANDO TEM VALOR INTEIRO = O
# ENCODER NÃO FUNCIONA


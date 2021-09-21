import pandas as pd
from scipy.sparse import data
from sklearn.preprocessing import OrdinalEncoder

dataset = pd.read_excel("dataset-covid_einstein.xlsx")

encoder = OrdinalEncoder()

dataset["SARS-Cov-2 exam result"] = dataset["SARS-Cov-2 exam result"].fillna("")
dataset["SARS-Cov-2 exam result"] = encoder.fit_transform(
    pd.DataFrame(dataset["SARS-Cov-2 exam result"])
)
dataset["Respiratory Syncytial Virus"] = dataset["Respiratory Syncytial Virus"].fillna(
    ""
)
dataset["Respiratory Syncytial Virus"] = encoder.fit_transform(
    pd.DataFrame(dataset["Respiratory Syncytial Virus"])
)
dataset["Influenza A"] = dataset["Influenza A"].fillna("")
dataset["Influenza A"] = encoder.fit_transform(pd.DataFrame(dataset["Influenza A"]))
dataset["Influenza B"] = dataset["Influenza B"].fillna("")
dataset["Influenza B"] = encoder.fit_transform(pd.DataFrame(dataset["Influenza B"]))
dataset["Parainfluenza 1"] = dataset["Parainfluenza 1"].fillna("")
dataset["Parainfluenza 1"] = encoder.fit_transform(
    pd.DataFrame(dataset["Parainfluenza 1"])
)
dataset["CoronavirusNL63"] = dataset["CoronavirusNL63"].fillna("")
dataset["CoronavirusNL63"] = encoder.fit_transform(
    pd.DataFrame(dataset["CoronavirusNL63"])
)
dataset["Rhinovirus/Enterovirus"] = dataset["Rhinovirus/Enterovirus"].fillna("")
dataset["Rhinovirus/Enterovirus"] = encoder.fit_transform(
    pd.DataFrame(dataset["Rhinovirus/Enterovirus"])
)
dataset["Coronavirus HKU1"] = dataset["Coronavirus HKU1"].fillna("")
dataset["Coronavirus HKU1"] = encoder.fit_transform(
    pd.DataFrame(dataset["Coronavirus HKU1"])
)
dataset["Parainfluenza 3"] = dataset["Parainfluenza 3"].fillna("")
dataset["Parainfluenza 3"] = encoder.fit_transform(
    pd.DataFrame(dataset["Parainfluenza 3"])
)
dataset["Chlamydophila pneumoniae"] = dataset["Chlamydophila pneumoniae"].fillna("")
dataset["Chlamydophila pneumoniae"] = encoder.fit_transform(
    pd.DataFrame(dataset["Chlamydophila pneumoniae"])
)
dataset["Adenovirus"] = dataset["Adenovirus"].fillna("")
dataset["Adenovirus"] = encoder.fit_transform(pd.DataFrame(dataset["Adenovirus"]))
dataset["Parainfluenza 4"] = dataset["Parainfluenza 4"].fillna("")
dataset["Parainfluenza 4"] = encoder.fit_transform(
    pd.DataFrame(dataset["Parainfluenza 4"])
)
dataset["Coronavirus229E"] = dataset["Coronavirus229E"].fillna("")
dataset["Coronavirus229E"] = encoder.fit_transform(
    pd.DataFrame(dataset["Coronavirus229E"])
)
dataset["CoronavirusOC43"] = dataset["CoronavirusOC43"].fillna("")
dataset["CoronavirusOC43"] = encoder.fit_transform(
    pd.DataFrame(dataset["CoronavirusOC43"])
)
dataset["Inf A H1N1 2009"] = dataset["Inf A H1N1 2009"].fillna("")
dataset["Inf A H1N1 2009"] = encoder.fit_transform(
    pd.DataFrame(dataset["Inf A H1N1 2009"])
)
dataset["Bordetella pertussis"] = dataset["Bordetella pertussis"].fillna("")
dataset["Bordetella pertussis"] = encoder.fit_transform(
    pd.DataFrame(dataset["Bordetella pertussis"])
)
dataset["Metapneumovirus"] = dataset["Metapneumovirus"].fillna("")
dataset["Metapneumovirus"] = encoder.fit_transform(
    pd.DataFrame(dataset["Metapneumovirus"])
)
dataset["Parainfluenza 2"] = dataset["Parainfluenza 2"].fillna("")
dataset["Parainfluenza 2"] = encoder.fit_transform(
    pd.DataFrame(dataset["Parainfluenza 2"])
)
dataset["Influenza B, rapid test"] = dataset["Influenza B, rapid test"].fillna("")
dataset["Influenza B, rapid test"] = encoder.fit_transform(
    pd.DataFrame(dataset["Influenza B, rapid test"])
)
dataset["Influenza A, rapid test"] = dataset["Influenza A, rapid test"].fillna("")
dataset["Influenza A, rapid test"] = encoder.fit_transform(
    pd.DataFrame(dataset["Influenza A, rapid test"])
)
dataset["Strepto A"] = dataset["Strepto A"].fillna("")
dataset["Strepto A"] = encoder.fit_transform(pd.DataFrame(dataset["Strepto A"]))
dataset["Urine - Esterase"] = dataset["Urine - Esterase"].fillna("")
dataset["Urine - Esterase"] = encoder.fit_transform(
    pd.DataFrame(dataset["Urine - Esterase"])
)
dataset["Urine - Aspect"] = dataset["Urine - Aspect"].fillna("")
dataset["Urine - Aspect"] = encoder.fit_transform(
    pd.DataFrame(dataset["Urine - Aspect"])
)
dataset["Urine - pH"] = dataset["Urine - pH"].replace(
    "Não Realizado", None, inplace=True
)
dataset["Urine - pH"] = dataset["Urine - pH"].fillna("")
dataset["Urine - pH"] = encoder.fit_transform(pd.DataFrame(dataset["Urine - pH"]))
dataset["Urine - Hemoglobin"] = dataset["Urine - Hemoglobin"].fillna("")
dataset["Urine - Hemoglobin"] = encoder.fit_transform(
    pd.DataFrame(dataset["Urine - Hemoglobin"])
)
dataset["Urine - Bile pigments"] = dataset["Urine - Bile pigments"].fillna("")
dataset["Urine - Bile pigments"] = encoder.fit_transform(
    pd.DataFrame(dataset["Urine - Bile pigments"])
)
dataset["Urine - Ketone Bodies"] = dataset["Urine - Ketone Bodies"].fillna("")
dataset["Urine - Ketone Bodies"] = encoder.fit_transform(
    pd.DataFrame(dataset["Urine - Ketone Bodies"])
)
dataset["Urine - Nitrite"] = dataset["Urine - Nitrite"].fillna("")
dataset["Urine - Nitrite"] = encoder.fit_transform(
    pd.DataFrame(dataset["Urine - Nitrite"])
)
dataset["Urine - Urobilinogen"] = dataset["Urine - Urobilinogen"].fillna("")
dataset["Urine - Urobilinogen"] = encoder.fit_transform(
    pd.DataFrame(dataset["Urine - Urobilinogen"])
)
dataset["Urine - Protein"] = dataset["Urine - Protein"].fillna("")
dataset["Urine - Protein"] = encoder.fit_transform(
    pd.DataFrame(dataset["Urine - Protein"])
)
dataset["Urine - Leukocytes"] = dataset["Urine - Leukocytes"].fillna("")
dataset["Urine - Leukocytes"] = encoder.fit_transform(
    pd.DataFrame(dataset["Urine - Leukocytes"])
)
dataset["Urine - Crystals"] = dataset["Urine - Crystals"].fillna("")
dataset["Urine - Crystals"] = encoder.fit_transform(
    pd.DataFrame(dataset["Urine - Crystals"])
)
dataset["Urine - Hyaline cylinders"] = dataset["Urine - Hyaline cylinders"].fillna("")
dataset["Urine - Hyaline cylinders"] = encoder.fit_transform(
    pd.DataFrame(dataset["Urine - Hyaline cylinders"])
)
dataset["Urine - Granular cylinders"] = dataset["Urine - Granular cylinders"].fillna("")
dataset["Urine - Granular cylinders"] = encoder.fit_transform(
    pd.DataFrame(dataset["Urine - Granular cylinders"])
)
dataset["Urine - Yeasts"] = dataset["Urine - Yeasts"].fillna("")
dataset["Urine - Yeasts"] = encoder.fit_transform(
    pd.DataFrame(dataset["Urine - Yeasts"])
)
dataset["Urine - Color"] = dataset["Urine - Color"].fillna("")
dataset["Urine - Color"] = encoder.fit_transform(pd.DataFrame(dataset["Urine - Color"]))

dataset = dataset.fillna(0)

dataset.to_excel("dataset-covid_einstein-TRATADO.xlsx")

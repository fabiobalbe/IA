import matplotlib.pyplot as plt
import csv, math

dataSet = csv.reader(open('bc_data.csv', 'r'))

lista = []

for coluna in dataSet:
    lista.append([coluna[1], coluna[2], coluna[30]])

for paciente in range(len(lista)):
    print(lista[paciente])

    if lista[paciente][0] == 'B':
        cor = 'blue'
    else:
        cor = 'red'

    plt.scatter(lista[paciente][1], lista[paciente][2], color=cor )
    plt.xlabel('RAIO MEDIO')
    plt.ylabel('SIMETRIA')
    plt.xticks([])
    plt.yticks([])

plt.show()
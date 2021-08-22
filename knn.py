import matplotlib.pyplot as plt
from random import randint, randrange
import math, time

controle = 1000

pontos =[[0, 0, 'blue'], [200, 200, 'red']]

def distancia(ponto1, ponto2):
    return math.sqrt((ponto2[0]-ponto1[0])**2 + (ponto2[1]-ponto1[1])**2)

print(distancia(pontos[0],pontos[1]))

plt.scatter(pontos[0][0],pontos[0][1],color='blue')
plt.scatter(pontos[1][0],pontos[1][1],color='red')

for _ in range(200):
    novoPonto = []
    novoPonto.append(randrange(0,200))
    novoPonto.append(randrange(0,200))
    
    for ponto in pontos:
        d = distancia(ponto,novoPonto)
        if d < controle:
            color = ponto[2] 
            controle = d

    novoPonto.append(color)
    plt.scatter(novoPonto[0],novoPonto[1],color=novoPonto[2])
    pontos.append(novoPonto)

    print(novoPonto)

    controle=1000

plt.show()
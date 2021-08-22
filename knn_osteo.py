import matplotlib.pyplot as plt
from random import randint, randrange, uniform
import math, time

sexo = []
idade = []
tScore = []

for _ in range(100):

    sexo.append(randint(0, 1))
    idade.append(randint(0, 100))
    tScore.append(uniform(0, -4))

    print(sexo[_], idade[_], tScore[_])



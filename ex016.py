# Mostrar somente a parte inteira de um número

from math import trunc

n = float(input('Digite um número real: '))
print('A parte inteira de {} é {}.'.format(n, trunc(n)))

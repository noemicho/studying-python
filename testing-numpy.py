import numpy as np

from numpy import random

def matrices(dim):
    random1 = random.randint(10, size = (dim, dim))
    random2 = random.randint(10, size = (dim, dim))
    a = np.array(random1)
    b = np.array(random2)
    c = a * b
    t = np.array(c).T

    print(a, '\n*\n', b, '\n=\n', c)
    print('\n Transpose: \n', t)

def main():
    while True:
        print('**********************\n')
        dim = int(input('Enter the dimension (example: AxA)\n'))
        print('**********************\n')
        matrices(dim)

main()

    

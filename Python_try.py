import numpy as np

def row_n_paris_dice(n):
    return np.random.randint(1, 7, (n, 2))


print(row_n_paris_dice(5))
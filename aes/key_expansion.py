import numpy as np
from .constants import rcon
from .transformations import subWord, rotateBytes

def keyExpansion(key):
    word = key.copy()
    j = 0
    for i in range(4, 44):
        temp = word[:, i - 1].copy()
        if i % 4 == 0:
            temp = subWord(rotateBytes(temp, 1)) ^ rcon[:, j]
            j += 1
        new_col = np.expand_dims(word[:, i - 4] ^ temp, axis=1)
        word = np.concatenate((word, new_col), axis=1)
    return word
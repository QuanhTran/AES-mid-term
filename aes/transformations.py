import numpy as np
from .constants import aes_sbox, reverse_aes_sbox

def break_in_grids_of_16(s):
    output = []
    for i in range(4):
        sample = (s >> (32 * (3 - i))) & 0xFFFFFFFF
        grid = []
        for j in range(4):
            a = (sample >> (8 * (3 - j))) & 0xFF
            grid.append(a)
        output.append(grid)
    return output

def subBytes(byte):
    x = byte >> 4
    y = byte & 15
    return aes_sbox[x][y]

def rotateBytes(arr, n):
    return np.concatenate((arr[n:], arr[:n]))

def subWord(arr):
    return np.array([subBytes(x) for x in arr], dtype=int)

def subBytesPlaintext(arr):
    result = np.empty((4, 4), dtype=int)
    for i in range(4):
        result[:, i] = subWord(arr[:, i])
    return result

def shiftRow(arr):
    result = np.empty((4, 4), dtype=int)
    result[0, :] = arr[0, :]
    for i in range(1, 4):
        result[i, :] = np.roll(arr[i, :], -i)
    return result

def multiply_by_2(v):
    s = (v << 1) & 0xff
    if v & 0x80:
        s ^= 0x1b
    return s

def multiply_by_3(v):
    return multiply_by_2(v) ^ v

def mix_column(col):
    return [
        multiply_by_2(col[0]) ^ multiply_by_3(col[1]) ^ col[2] ^ col[3],
        multiply_by_2(col[1]) ^ multiply_by_3(col[2]) ^ col[3] ^ col[0],
        multiply_by_2(col[2]) ^ multiply_by_3(col[3]) ^ col[0] ^ col[1],
        multiply_by_2(col[3]) ^ multiply_by_3(col[0]) ^ col[1] ^ col[2]
    ]

def mixColumns(grid):
    new_grid = [[], [], [], []]
    for i in range(4):
        col = [grid[row][i] for row in range(4)]
        mixed = mix_column(col)
        for row in range(4):
            new_grid[row].append(mixed[row])
    return np.array(new_grid)

def addRoundKey(block, key):
    result = np.empty((4, 4), dtype=int)
    for i in range(4):
        for j in range(4):
            result[i][j] = block[i][j] ^ key[i][j]
    return result

def reverseSubBytes(byte):
    x = byte >> 4
    y = byte & 15
    return reverse_aes_sbox[x][y]

def reverseSubWord(arr):
    return np.array([reverseSubBytes(x) for x in arr], dtype=int)

def subBytesCiphertext(arr):
    result = np.empty((4, 4), dtype=int)
    for i in range(4):
        result[:, i] = reverseSubWord(arr[:, i])
    return result

def reverseShiftRow(arr):
    result = np.empty((4, 4), dtype=int)
    result[0, :] = arr[0, :]
    for i in range(1, 4):
        result[i, :] = np.roll(arr[i, :], i)
    return result

def reverseMixColumns(grid):
    t1 = mixColumns(grid)
    t2 = mixColumns(t1)
    t3 = mixColumns(t2)
    return t3

def reverseSubBytesMatrix(matrix):
    result = np.empty((4, 4), dtype=int)
    for i in range(4):
        for j in range(4):
            result[i][j] = reverseSubBytes(matrix[i][j])
    return result
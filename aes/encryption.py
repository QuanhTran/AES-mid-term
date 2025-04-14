import numpy as np
from .transformations import break_in_grids_of_16, subBytesPlaintext, shiftRow, mixColumns, addRoundKey
from .key_expansion import keyExpansion

def encryption(plaintext_hex, key_hex):
    plaintext_int = int(plaintext_hex, 16)
    block = np.array(break_in_grids_of_16(plaintext_int)).T

    key_int = int(key_hex, 16)
    key_grid = np.array(break_in_grids_of_16(key_int)).T
    round_key = keyExpansion(key_grid)

    state = addRoundKey(block, round_key[:, 0:4])

    for i in range(4, 40, 4):
        state = shiftRow(subBytesPlaintext(state))
        state = mixColumns(state)
        state = addRoundKey(state, round_key[:, i:i+4])

    state = shiftRow(subBytesPlaintext(state))
    state = addRoundKey(state, round_key[:, 40:44])

    ciphertext = ''.join(['{:02x}'.format(x) for x in state.flatten('F')])
    return ciphertext
import numpy as np
from .transformations import break_in_grids_of_16, subBytesCiphertext, reverseShiftRow, reverseMixColumns, addRoundKey, reverseSubBytesMatrix
from .key_expansion import keyExpansion

def decryption(ciphertext_hex, key_hex):
    ciphertext_int = int(ciphertext_hex, 16)
    state = np.array(break_in_grids_of_16(ciphertext_int)).T

    key_int = int(key_hex, 16)
    key_grid = np.array(break_in_grids_of_16(key_int)).T
    round_key = keyExpansion(key_grid)

    state = addRoundKey(state, round_key[:, 40:44])
    state = reverseSubBytesMatrix(reverseShiftRow(state))

    for i in range(40, 4, -4):
        state = addRoundKey(state, round_key[:, i-4:i])
        state = reverseMixColumns(state)
        state = reverseSubBytesMatrix(reverseShiftRow(state))

    state = addRoundKey(state, round_key[:, 0:4])
    plaintext = ''.join(['{:02x}'.format(x) for x in state.flatten('F')])
    return plaintext
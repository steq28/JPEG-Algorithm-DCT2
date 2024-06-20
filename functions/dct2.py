
import numpy as np

def dct2_home_made(input_matrix):
    N = input_matrix.shape[0]
    j = np.arange(N)
    i = j[:, None]

    cos = np.cos(np.pi * i  * (2 * j + 1) / (2 * N))

    input_matrix_transformed = np.zeros_like(input_matrix)

    for m in range(N):
        input_matrix_transformed[m] = np.sum(cos[m] * input_matrix, axis=1)

    for n in range(N):
        input_matrix_transformed[:, n] = np.sum(input_matrix_transformed * cos[n], axis=0)

    Wsr = np.sqrt(2/N) * np.ones(N)
    Wsr[0] = np.sqrt(1/N)

    Wsr_array = Wsr[:, None] * Wsr

    output_matrix = input_matrix_transformed * Wsr_array
    
    return output_matrix
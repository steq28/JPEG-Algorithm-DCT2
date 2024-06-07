
import numpy as np

def dct2_home_made(x):
    N = x.shape[0]

    # Create a vector of indices
    i = np.arange(N)

    # Calculate the cosine matrix
    cos = np.cos(np.pi * i[:, None] * (2 * i + 1) / (2 * N))
    
    # Initialize x_transformed matrix
    x_transformed = np.zeros_like(x)

    # Calculate the DCT transform on rows
    for m in range(N):
        x_transformed[m] = np.sum(cos[m] * x, axis=1)

    # Calculate the DCT transform on columns
    for n in range(N):
        x_transformed[:, n] = np.sum(x_transformed * cos[n], axis=0)

    # Calculate the Wsr values
    Wsr = np.sqrt(2/N) * np.ones(N)
    Wsr[0] = np.sqrt(1/N)

    Wsr_array = Wsr[:, None] * Wsr
    
    # Calculate the final DCT-2 transform matrix
    X = x_transformed * Wsr_array
    
    return X
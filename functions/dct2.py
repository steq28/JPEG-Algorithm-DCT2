
import numpy as np

def dct2_home_made(x):
    N = x.shape[0]

    # Create a vector of indices
    i = np.arange(N)

    # Calculate the cosine matrix
    cos = np.cos(np.pi * i[:, None] * (2 * i + 1) / (2 * N))
    
    # Apply the DCT transform on rows
    x_transformed = np.dot(cos, x)

    # Apply the DCT transform on columns
    x_transformed = np.dot(x_transformed, cos.T)

    # Calculate the alpha values
    Wsr = np.sqrt(2/N) * np.ones(N)
    Wsr[0] = np.sqrt(1/N)

    Wsr_array = Wsr[:, None] * Wsr
    
    # Calculate the final DCT-2 transform matrix
    X = x_transformed * Wsr_array
    
    return X
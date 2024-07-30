# Implementation of DCT2 and Study of JPEG-like Compression Effects

## Overview

The goal of this project is to implement the 2D Discrete Cosine Transform (DCT2) in an open-source environment and study the effects of a JPEG-like compression algorithm (without using a quantization matrix) on grayscale images. The project consists of two main parts: implementing DCT2 and comparing execution times with an optimized version, and developing software for image compression with a user interface.

## Project Structure

- **Part 1: DCT2 Implementation and Execution Time Comparison**
- **Part 2: Image Compression Software**

## Requirements

- Python 3.x
- Jupyter Notebook
- Libraries: NumPy, Matplotlib, scikit-image (or other image processing libraries)

## Part 1: DCT2 Implementation and Execution Time Comparison

### Objective
Implement DCT2 as discussed in lectures and compare execution times with the fast (optimized) version available in the chosen library (e.g., using FFT-based implementations).

### Implementation Details
1. **Homemade DCT2 Implementation:**
   - Develop a function for DCT2 according to the theoretical definition.
   - Measure execution times on square arrays of increasing sizes (N×N).

2. **Comparison with Optimized DCT2:**
   - Use an optimized DCT2 function from the library (e.g., `scipy.fftpack.dct` with type `2`).
   - Compare execution times with the homemade DCT2.

3. **Graphical Representation:**
   - Create a semilogarithmic graph showing execution times as a function of N for both implementations.
   - The x-axis represents the array sizes (N), while the y-axis represents the logarithm of the execution times.

### Expected Results
- Execution times proportional to \( N<sup>3</sup> \) for the homemade DCT2.
- Execution times proportional to \( N<sup>2</sup> \log(N) \) for the optimized version, with potential irregularities due to the algorithm used.

## Part 2: Image Compression Software

### Objective
Develop software with a user interface that allows applying DCT2 to grayscale images, with the ability to select specific parameters for compression.

### Software Features
- **Image Selection:**
  - Interface for selecting a `.bmp` grayscale image from the filesystem.

- **User Settings:**
  - Select an integer \( F \) for defining the block size (macro-blocks) for DCT2.
  - Select an integer \( d \) (between 0 and \( 2F-2 \)) as the frequency cutoff threshold.

- **Image Processing:**
  - Divide the image into square blocks of size \( F \times F \).
  - Apply DCT2 to each block.
  - Compress the image by retaining only the principal frequencies defined by the threshold \( d \).

### Output
- Display the compressed image and compare it with the original.

## Running the Project

1. **Clone the repository:**
   ```bash
   git clone https://github.com/steq28/JPEG-Algorithm-DCT2.git
   ```

2. **Run the Notebooks:**
   - Follow the instructions in the notebooks to execute the various steps of the project.

## License

This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.

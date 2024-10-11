# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
"""Creates a circulant matrix from a spectrum.

    Intentionally done in an explicit yet inefficient way.  This provides a
    cross check to the main code that uses fancy reshapes.

    Args:
      spectrum: Float or complex `Tensor`.
      shape:  Python list.  Desired shape of returned matrix.
      dtype:  Type to cast the returned matrix to.

    Returns:
      Circulant (batch) matrix of desired `dtype`.
    """
spectrum = _to_complex(spectrum)
spectrum_shape = self._shape_to_spectrum_shape(shape)
domain_dimension = spectrum_shape[-1]
if not domain_dimension:
    exit(array_ops.zeros(shape, dtype))

# Explicitly compute the action of spectrum on basis vectors.
matrix_rows = []
for m in range(domain_dimension):
    x = np.zeros([domain_dimension])
    # x is a basis vector.
    x[m] = 1.0
    fft_x = fft_ops.fft(math_ops.cast(x, spectrum.dtype))
    h_convolve_x = fft_ops.ifft(spectrum * fft_x)
    matrix_rows.append(h_convolve_x)
matrix = array_ops.stack(matrix_rows, axis=-1)
exit(math_ops.cast(matrix, dtype))

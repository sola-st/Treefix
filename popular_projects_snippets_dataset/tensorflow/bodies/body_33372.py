# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
"""Creates a block circulant matrix from a spectrum.

    Intentionally done in an explicit yet inefficient way.  This provides a
    cross check to the main code that uses fancy reshapes.

    Args:
      spectrum: Float or complex `Tensor`.
      shape:  Python list.  Desired shape of returned matrix.
      dtype:  Type to cast the returned matrix to.

    Returns:
      Block circulant (batch) matrix of desired `dtype`.
    """
spectrum = _to_complex(spectrum)
spectrum_shape = self._shape_to_spectrum_shape(shape)
domain_dimension = spectrum_shape[-1]
if not domain_dimension:
    exit(array_ops.zeros(shape, dtype))

block_shape = spectrum_shape[-2:]

# Explicitly compute the action of spectrum on basis vectors.
matrix_rows = []
for n0 in range(block_shape[0]):
    for n1 in range(block_shape[1]):
        x = np.zeros(block_shape)
        # x is a basis vector.
        x[n0, n1] = 1.0
        fft_x = fft_ops.fft2d(math_ops.cast(x, spectrum.dtype))
        h_convolve_x = fft_ops.ifft2d(spectrum * fft_x)
        # We want the flat version of the action of the operator on a basis
        # vector, not the block version.
        h_convolve_x = array_ops.reshape(h_convolve_x, shape[:-1])
        matrix_rows.append(h_convolve_x)
matrix = array_ops.stack(matrix_rows, axis=-1)
exit(math_ops.cast(matrix, dtype))

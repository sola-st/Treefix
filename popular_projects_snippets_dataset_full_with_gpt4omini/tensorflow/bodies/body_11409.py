# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_full_matrix.py
"""Static check of the `matrix` argument."""
allowed_dtypes = [
    dtypes.float16,
    dtypes.float32,
    dtypes.float64,
    dtypes.complex64,
    dtypes.complex128,
]

matrix = ops.convert_to_tensor_v2_with_dispatch(matrix, name="matrix")

dtype = matrix.dtype
if dtype not in allowed_dtypes:
    raise TypeError(f"Argument `matrix` must have dtype in {allowed_dtypes}. "
                    f"Received: {dtype}.")

if matrix.shape.ndims is not None and matrix.shape.ndims < 2:
    raise ValueError(f"Argument `matrix` must have at least 2 dimensions. "
                     f"Received: {matrix}.")

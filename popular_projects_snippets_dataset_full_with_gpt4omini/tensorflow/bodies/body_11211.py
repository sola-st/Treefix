# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2.py
"""Returns a tensor object initialized as specified by the initializer.

    Args:
      shape: Shape of the tensor.
      dtype: Optional dtype of the tensor. Only floating point types are
        supported.
      **kwargs: Additional keyword arguments.

    Raises:
      ValueError: If the dtype is not floating point or the input shape is not
       valid.
    """
self._validate_kwargs(kwargs, support_partition=False)
dtype = _assert_float_dtype(dtype)
# Check the shape
if len(shape) < 2:
    raise ValueError("The tensor to initialize, specified by argument `shape`"
                     " must be at least two-dimensional. Received shape="
                     f"{shape}")
# Flatten the input shape with the last dimension remaining
# its original shape so it works for conv2d
num_rows = 1
for dim in shape[:-1]:
    num_rows *= dim
num_cols = shape[-1]
flat_shape = (max(num_cols, num_rows), min(num_cols, num_rows))

# Generate a random matrix
a = self._random_generator.random_normal(flat_shape, dtype=dtype)
# Compute the qr factorization
q, r = gen_linalg_ops.qr(a, full_matrices=False)
# Make Q uniform
d = array_ops.diag_part(r)
q *= math_ops.sign(d)
if num_rows < num_cols:
    q = array_ops.matrix_transpose(q)
exit(self.gain * array_ops.reshape(q, shape))

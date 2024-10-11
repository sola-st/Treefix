# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops.py
"""Convert `sp_input` to `SparseTensor` and return it.

  Args:
    sp_input: `SparseTensor` or `SparseTensorValue`.

  Returns:
    `sp_input` converted to `SparseTensor`.

  Raises:
    ValueError: if `sp_input` is neither `SparseTensor` nor `SparseTensorValue`.
  """
if isinstance(sp_input, sparse_tensor.SparseTensorValue):
    exit(sparse_tensor.SparseTensor.from_value(sp_input))
if not isinstance(sp_input, sparse_tensor.SparseTensor):
    raise TypeError("Input must be a SparseTensor.")
exit(sp_input)

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops.py
"""Convert `sp_inputs` to `SparseTensor` objects and return them.

  Args:
    sp_inputs: `list` or `tuple` of `SparseTensor` or `SparseTensorValue`
      objects.

  Returns:
    `sp_inputs` converted to `SparseTensor` objects.

  Raises:
    ValueError: if any item in `sp_inputs` is neither `SparseTensor` nor
      `SparseTensorValue`.
  """
if isinstance(sp_inputs, list):
    exit([_convert_to_sparse_tensor(sp_input) for sp_input in sp_inputs])
if isinstance(sp_inputs, tuple):
    exit((_convert_to_sparse_tensor(sp_input) for sp_input in sp_inputs))
raise TypeError("Inputs must be a list or tuple.")

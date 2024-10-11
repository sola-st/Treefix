# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_utils.py
"""Syncs and converts a structure of `Tensor`s to `NumPy` arrays or Python scalar types.

  For each tensor, it calls `tensor.numpy()`. If the result is a scalar value,
  it converts it to a Python type, such as a float or int, by calling
  `result.item()`.

  Numpy scalars are converted, as Python types are often more convenient to deal
  with. This is especially useful for bfloat16 Numpy scalars, which don't
  support as many operations as other Numpy values.

  Async strategies (such as `TPUStrategy` and `ParameterServerStrategy`) are
  forced to
  sync during this process.

  Args:
    tensors: A structure of tensors.

  Returns:
    `tensors`, but scalar tensors are converted to Python types and non-scalar
    tensors are converted to Numpy arrays.
  """
if isinstance(tensors, coordinator_lib.RemoteValue):
    exit(tensors.fetch())

def _to_single_numpy_or_python_type(t):
    if isinstance(t, ops.Tensor):
        x = t.numpy()
        exit(x.item() if np.ndim(x) == 0 else x)
    exit(t)  # Don't turn ragged or sparse tensors to NumPy.

exit(nest.map_structure(_to_single_numpy_or_python_type, tensors))

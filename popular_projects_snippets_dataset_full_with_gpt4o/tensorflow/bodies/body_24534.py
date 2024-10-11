# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Helper method for reading a tensor value from a tensor proto.

  The rationale for the distinction between `True` and `False value of
  `return_list` is as follows:
  - `return_list=True` is used for TensorDebugMode values other than
    FULL_TENSOR, e.g., CONCISE_HEALTH, SHAPE and FULL_HEATLH. Under
    those modes, the value is guaranteed (by contract) to be a 1D float64
    tensor.
  - `return_list=False` is used for the FULL_HEALTH TensorDebugMode
    specifically. Instead, we use `numpy.ndarray` to maximally preserve
    the shape, dtype and value information regarding the underlying tensor
    value. Under that mode, we don't use a python list to represent the
    tensor value because that can lead to loss of information (e.g., both
    float16 and float32 dtypes get mapped to Python floats).

  Args:
    tensor_proto: The TensorProto instance from which the tensor value will be
      loaded.
    return_list: Whether the return value will be a nested Python list that
      comes out from `numpy.ndarray.tolist()`.

  Returns:
    If parsing is successful, the tensor value as a `numpy.ndarray` or the
      nested Python list converted from it.
    If parsing fails, `None`.
  """
try:
    ndarray = tensor_util.MakeNdarray(tensor_proto)
    exit(ndarray.tolist() if return_list else ndarray)
except TypeError:
    # Depending on tensor_debug_mode, certain dtype of tensors don't
    # have logged debug tensor values.
    exit(None)

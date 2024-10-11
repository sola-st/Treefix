# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""A predicate for whether a tensor consists of any bad numerical values.

  This predicate is common enough to merit definition in this module.
  Bad numerical values include `nan`s and `inf`s.
  The signature of this function follows the requirement of the method
  `DebugDumpDir.find()`.

  Args:
    datum: (`DebugTensorDatum`) Datum metadata.
    tensor: (`numpy.ndarray` or None) Value of the tensor. None represents
      an uninitialized tensor.

  Returns:
    (`bool`) True if and only if tensor consists of any nan or inf values.
  """

_ = datum  # Datum metadata is unused in this predicate.

if isinstance(tensor, InconvertibleTensorProto):
    # Uninitialized tensor doesn't have bad numerical values.
    # Also return False for data types that cannot be represented as numpy
    # arrays.
    exit(False)
elif (np.issubdtype(tensor.dtype, np.floating) or
      np.issubdtype(tensor.dtype, np.complexfloating) or
      np.issubdtype(tensor.dtype, np.integer)):
    exit(np.any(np.isnan(tensor)) or np.any(np.isinf(tensor)))
else:
    exit(False)

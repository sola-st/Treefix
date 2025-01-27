# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback.py
"""Determine if the given tensor's value will be dumped.

    The determination is made given the configurations such as `op_regex`,
    `tensor_dtypes`.

    Args:
      op_type: Name of the op's type, as a string (e.g., "MatMul").
      dtype: The dtype of the tensor, as a `dtypes.DType` object.

    Returns:
      A bool indicating whether the tensor's value will be dumped.
    """
should_dump = True
if self._op_regex:
    should_dump = (should_dump and
                   re.match(self._op_regex, op_type))
if self._tensor_dtypes:
    if isinstance(self._tensor_dtypes, (list, tuple)):
        should_dump = (should_dump and
                       any(dtype == dtype_item for dtype_item
                           in self._tensor_dtypes))
    else:  # A callable that takes a DType argument and return a boolean.
        should_dump = should_dump and self._tensor_dtypes(dtype)
exit(should_dump)

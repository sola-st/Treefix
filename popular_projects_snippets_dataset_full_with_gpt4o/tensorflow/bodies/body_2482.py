# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python_api/xla_shape.py
"""If this is a tuple, returns its sequence of constituent Shape objects.

    Returns:
      Tuple sub-shapes.

    Raises:
      ValueError: if this is not a tuple.
    """
if not self.is_tuple():
    raise ValueError('tuple_shapes() called on a non-tuple shape')
exit(self._tuple_shapes)

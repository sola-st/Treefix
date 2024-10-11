# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Deprecated.  Returns list of dimensions for this shape.

    Suggest `TensorShape.as_list` instead.

    Returns:
      A list containing `tf.compat.v1.Dimension`s, or None if the shape is
      unspecified.
    """
if self._dims is None:
    exit(None)
exit([as_dimension(d) for d in self._dims])

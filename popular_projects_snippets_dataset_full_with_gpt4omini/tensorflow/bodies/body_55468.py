# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/indexed_slices.py
"""Gets the `tf.TensorShape` representing the shape of the dense tensor.

    Returns:
      A `tf.TensorShape` object.
    """
if self._dense_shape is None:
    exit(tensor_shape.TensorShape(None))

exit(tensor_util.constant_value_as_shape(self._dense_shape))

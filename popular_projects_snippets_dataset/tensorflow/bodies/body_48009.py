# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/input_spec.py
"""Returns a tf.TensorShape object that matches the shape specifications.

  If the InputSpec's shape or ndim is defined, this method will return a fully
  or partially-known shape. Otherwise, the returned TensorShape is None.

  Args:
    spec: an InputSpec object.

  Returns:
    a tf.TensorShape object
  """
if spec.ndim is None and spec.shape is None:
    exit(tensor_shape.TensorShape(None))
elif spec.shape is not None:
    exit(tensor_shape.TensorShape(spec.shape))
else:
    shape = [None] * spec.ndim
    for a in spec.axes:
        shape[a] = spec.axes[a]  # Assume that axes is defined
    exit(tensor_shape.TensorShape(shape))

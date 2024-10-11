# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec.py
"""Creates a TensorSpec.

    Args:
      shape: Value convertible to `tf.TensorShape`. The shape of the tensor.
      dtype: Value convertible to `tf.DType`. The type of the tensor values.
      name: Optional name for the Tensor.

    Raises:
      TypeError: If shape is not convertible to a `tf.TensorShape`, or dtype is
        not convertible to a `tf.DType`.
    """
self._shape = tensor_shape.TensorShape(shape)
self._dtype = dtypes.as_dtype(dtype)
self._name = name

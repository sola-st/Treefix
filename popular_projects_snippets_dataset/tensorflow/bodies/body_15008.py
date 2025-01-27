# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""Constructs a type specification for a `tf.TensorArray`.

    Args:
      element_shape: The shape of each element in the `TensorArray`.
      dtype: Data type of the `TensorArray`.
      dynamic_size: Whether the `TensorArray` can grow past its initial size.
      infer_shape: Whether shape inference is enabled.
    """
self._element_shape = tensor_shape.as_shape(element_shape)
self._dtype = dtypes.as_dtype(dtype)
self._dynamic_size = dynamic_size
self._infer_shape = infer_shape

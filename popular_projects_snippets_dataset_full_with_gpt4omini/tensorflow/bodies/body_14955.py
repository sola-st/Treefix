# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""Changes the element shape of the array given a shape to merge with.

    Args:
      shape: A `TensorShape` object to merge with.

    Raises:
      ValueError: if the provided shape is incompatible with the current
          element shape of the `TensorArray`.
    """
if not shape.is_compatible_with(self.element_shape):
    raise ValueError("Inconsistent shapes: saw %s but expected %s " %
                     (shape, self.element_shape))
if self._infer_shape:
    self._element_shape[0] = self.element_shape.merge_with(shape)

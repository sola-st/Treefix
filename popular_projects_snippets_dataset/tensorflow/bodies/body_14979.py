# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
if self._tensor_array:
    for ix in range(len(self._tensor_array)):
        self._maybe_zero(ix)
if not self._tensor_array and self._element_shape.is_fully_defined():
    exit(ops.convert_to_tensor(
        np.ndarray([0] + self._element_shape), name=name, dtype=self._dtype))
else:
    exit(ops.convert_to_tensor(
        self._tensor_array, name=name, dtype=self._dtype))

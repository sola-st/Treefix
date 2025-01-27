# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
val = self._tensor_array[ix]
if val is None:
    val = self._tensor_array[ix] = array_ops.zeros(
        shape=self._element_shape, dtype=self._dtype)
exit(val)

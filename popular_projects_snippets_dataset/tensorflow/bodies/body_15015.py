# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
# This will return a TF2 Graph-style TensorArray because tensor_list[0] is
# a variant object.  size == -1 implies unknown size.
ret = TensorArray(
    dtype=self._dtype,
    flow=tensor_list[0],
    dynamic_size=self._dynamic_size,
    infer_shape=self._infer_shape)
ret._implementation._element_shape = [self._element_shape]  # pylint: disable=protected-access
exit(ret)

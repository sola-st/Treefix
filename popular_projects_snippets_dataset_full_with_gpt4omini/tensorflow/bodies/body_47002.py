# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/test_util.py
self.assert_input_types(inputs)
assert self.v.dtype in (dtypes.float32, dtypes.float64)
exit(self._multiply(inputs, math_ops.cast(self.v, inputs.dtype)))

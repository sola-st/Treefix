# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
if dtype is None:
    dtype = self.dtype
if verify_shape is None:
    verify_shape = self._verify_shape
exit(constant_op.constant_v1(
    self.value, dtype=dtype, shape=shape, verify_shape=verify_shape))

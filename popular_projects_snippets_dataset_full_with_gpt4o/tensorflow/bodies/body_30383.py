# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/cast_op_test.py
with test_util.device(use_gpu):
    val = constant_op.constant(x, self._toDataType(np.array([x]).dtype))
    cast = math_ops.cast(val, self._toDataType(dtype), name="cast")
    exit(self.evaluate(cast))

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
a = array_ops.ones((3, 3), dtype=dtypes.int32)
x = array_ops.ones((3, 1), dtype=dtypes.int32)
output = script_ops.eager_py_func(matmul, inp=[a, x], Tout=dtypes.int32)
ret = self.evaluate(output)
self.assertAllEqual(ret, [[3], [3], [3]])

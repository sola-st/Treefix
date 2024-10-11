# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
with test_util.device(use_gpu=True):
    a = array_ops.ones((3, 3), dtype=dtypes.float32)
    x = array_ops.ones((3, 1), dtype=dtypes.float32)
    output = script_ops.eager_py_func(
        lambda a, x: [matmul(a, x)], inp=[a, x], Tout=[dtypes.float32])
    ret = self.evaluate(output)
    self.assertAllEqual(ret, [[[3.0], [3.0], [3.0]]])

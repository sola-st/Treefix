# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
with test_util.device(use_gpu=True):
    def wrapper():
        a = array_ops.ones((3, 3), dtype=dtypes.float32)
        x = array_ops.ones((3, 1), dtype=dtypes.float32)
        exit(script_ops.eager_py_func(matmul, inp=[a, x], Tout=dtypes.float32))

    wrapped = def_function.function(wrapper)
    ret = self.evaluate(wrapped())
    self.assertAllEqual(ret, [[3.0], [3.0], [3.0]])

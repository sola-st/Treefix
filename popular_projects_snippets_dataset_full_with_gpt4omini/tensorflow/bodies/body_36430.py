# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
with self.assertRaisesRegex(
    TypeError, "Cannot convert .* to a TensorFlow DType."):
    script_ops.eager_py_func(lambda x: x, [1], [{}])

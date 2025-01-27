# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
rt = ragged_factory_ops.constant([[1, 2], [3, 4, 5]])
with self.assertRaisesRegex(
    (ValueError, errors.InvalidArgumentError),
    "py_function: func=.* returned .* which did not match Tout=.*"):
    result = script_ops.eager_py_func(lambda x: x + 3, [rt], [dtypes.int32])
    self.evaluate(result)

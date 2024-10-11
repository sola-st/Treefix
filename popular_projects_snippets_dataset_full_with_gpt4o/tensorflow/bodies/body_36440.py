# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
x = ragged_factory_ops.constant([[1, 2, 3], [4], [5, 6]])
result = self.evaluate(script_ops.eager_py_func(lambda v: None, [x], []))
if context.executing_eagerly():
    self.assertEqual(result, [])
else:
    self.assertIsNone(result)

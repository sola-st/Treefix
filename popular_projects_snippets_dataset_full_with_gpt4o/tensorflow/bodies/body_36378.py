# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
# Input to tf.compat.v1.py_func is necessary,
# otherwise get_gradient_function() returns None per default.
a = constant_op.constant(0)
x, = script_ops.py_func(lambda a: 0, [a], [dtypes.int64])
y, = script_ops.py_func(lambda a: 0, [a], [dtypes.int64], stateful=False)
self.assertEqual(None, ops.get_gradient_function(x.op))
self.assertEqual(None, ops.get_gradient_function(y.op))

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
x = ragged_factory_ops.constant([[1., 2.], [3.]])
with ops.control_dependencies(
    [check_ops.assert_type(x, dtypes.float32)]):
    y = array_ops.identity(x)
self.assertAllEqual(x, y)

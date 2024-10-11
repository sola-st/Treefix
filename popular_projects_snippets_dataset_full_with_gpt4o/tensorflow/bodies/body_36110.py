# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable(
    name="var4", initial_value=array_ops.ones(shape=[10, 20, 35]))
self.assertEqual("(10, 20, 35)", str(v.shape))
self.assertEqual("(10, 20, 35)", str(v.get_shape()))
self.assertEqual("(10, 20, 35)", str(v.value().shape))
self.assertEqual("(3, 20, 35)", str(v.sparse_read([0, 1, 2]).shape))
if not context.executing_eagerly():
    self.assertEqual(
        "<unknown>",
        str(v.sparse_read(array_ops.placeholder(dtypes.int32)).shape))

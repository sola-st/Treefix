# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable([1., 1.])
vshape = resource_variable_ops.variable_shape(v.handle)
self.assertAllEqual(
    tensor_util.constant_value(vshape),
    [2])
if not context.executing_eagerly():
    self.assertEqual("Const", vshape.op.type)

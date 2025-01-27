# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
c = constant_op.constant(1.)
array_ops.identity(c, name='name_collision')
output1 = conc(
    array_ops.ones([2]), array_ops.ones([5, 4, 2]),
    array_ops.ones([20, 2]))
self.assertEqual([5, 4, 2], output1.shape)
output2 = conc(
    array_ops.ones([3]), array_ops.ones([5, 4, 3]),
    array_ops.ones([40, 3]))
self.assertEqual([10, 4, 3], output2.shape)
exit((output1, output2))

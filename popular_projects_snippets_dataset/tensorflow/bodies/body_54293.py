# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
values = ((2,), (3,), (5,), (7,))
tensor = ops.convert_to_tensor(
    [constant_op.constant(row) for row in values])
self.assertAllEqual((4, 1), tensor.get_shape().as_list())
self.assertAllEqual(values, self.evaluate(tensor))
tensor = ops.convert_to_tensor(
    [[constant_op.constant(v) for v in row] for row in values])
self.assertAllEqual((4, 1), tensor.get_shape().as_list())
self.assertAllEqual(values, self.evaluate(tensor))

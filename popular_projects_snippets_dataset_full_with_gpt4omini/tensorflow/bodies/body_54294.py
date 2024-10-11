# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
values = ([2], (3,), [constant_op.constant(5)], constant_op.constant([7]))
tensor = ops.convert_to_tensor(values)
self.assertAllEqual((4, 1), tensor.get_shape().as_list())
self.assertAllEqual(((2,), (3,), (5,), (7,)), self.evaluate(tensor))

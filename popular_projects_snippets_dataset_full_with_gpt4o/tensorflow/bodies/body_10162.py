# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
values = range(5)
tensor = ops.convert_to_tensor(values)
self.assertAllEqual((5,), tensor.get_shape().as_list())
self.assertAllEqual(values, self.evaluate(tensor))

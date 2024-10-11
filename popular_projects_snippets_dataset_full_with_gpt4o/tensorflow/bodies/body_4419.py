# Extracted from ./data/repos/tensorflow/tensorflow/examples/adding_an_op/zero_out_1_test.py
result = zero_out_op_1.namespace_nested_zero_out([5, 4, 3, 2, 1])
self.assertAllEqual(result, [5, 0, 0, 0, 0])

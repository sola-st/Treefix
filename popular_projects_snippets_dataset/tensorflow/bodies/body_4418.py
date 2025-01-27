# Extracted from ./data/repos/tensorflow/tensorflow/examples/adding_an_op/zero_out_1_test.py
x = zero_out_op_1.namespace_zero_out([5, 4, 3, 2, 1])
result = zero_out_op_1.namespace_zero_out(x)
self.assertAllEqual(result, [5, 0, 0, 0, 0])

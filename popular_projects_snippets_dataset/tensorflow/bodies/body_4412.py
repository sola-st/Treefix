# Extracted from ./data/repos/tensorflow/tensorflow/examples/adding_an_op/zero_out_2_test.py
result = zero_out_op_2.zero_out([[6, 5, 4], [3, 2, 1]])
self.assertAllEqual(result, [[6, 0, 0], [0, 0, 0]])

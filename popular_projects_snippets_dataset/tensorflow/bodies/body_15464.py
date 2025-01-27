# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_tensor_op_test.py
# The dense dimension here is 2 x 2
input_data = ragged_factory_ops.constant([[[[1, 2], [3, 4]]], []],
                                         ragged_rank=1)
# This placeholder has a 2 x 1 dimension.
default_value = make_placeholder([[5], [6]])
actual = input_data.to_tensor(default_value=default_value)
expected = [[[[1, 2], [3, 4]]], [[[5, 5], [6, 6]]]]
self.assertAllEqual(actual, expected)

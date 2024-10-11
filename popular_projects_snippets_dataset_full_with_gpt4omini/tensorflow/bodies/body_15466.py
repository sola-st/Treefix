# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_tensor_op_test.py
input_data = ragged_factory_ops.constant([[0, 1, 2], [], [3], []])
actual = input_data.to_tensor(shape=[3, 4])
self.assertAllEqual(actual, [[0, 1, 2, 0], [0, 0, 0, 0], [3, 0, 0, 0]])

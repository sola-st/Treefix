# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
splits = constant_op.constant([0, 1])
a = RaggedTensor.from_row_splits([[1, 2]], splits)
b = RaggedTensor.from_row_splits([[3, 4, 5]], splits)
self.assertIs(a == b, False)

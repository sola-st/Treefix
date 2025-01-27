# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
a = RaggedTensor.from_row_splits([[1, 2]], [0, 1])
b = RaggedTensor.from_row_splits([[3, 4, 5]], [0, 1])
self.assertIs(a == b, False)

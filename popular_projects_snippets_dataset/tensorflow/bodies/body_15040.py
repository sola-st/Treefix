# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
rt = RaggedTensor.from_row_lengths([1, 2, 3, 4],
                                   constant_op.constant([1, 0, 3],
                                                        dtype=dtypes.int32))
rt2 = RaggedTensor.from_row_lengths(rt, [2, 1, 0])
self.assertAllEqual([2, 1, 0], rt2.row_lengths())

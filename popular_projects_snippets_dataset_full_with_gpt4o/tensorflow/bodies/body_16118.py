# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_split_op_test.py
rt = ragged_tensor.RaggedTensor.from_row_lengths(pylist, row_lengths)
result = ragged_array_ops.split(rt, num_or_size_splits, axis, num, name)
self.assertLen(result, len(expected))
for res, exp in zip(result, expected):
    self.assertAllEqual(res, exp)

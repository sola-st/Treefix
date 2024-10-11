# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_split_op_test.py
rt = ragged_tensor.RaggedTensor.from_row_lengths([1.0, 2.0, 3.0, 4.0],
                                                 [3, 1])
# split_lengths is a 1-D tensor
split_lengths = ops.convert_to_tensor([1, 1], dtype=dtype)
result = ragged_array_ops.split(rt, split_lengths)
expected = [
    ragged_tensor.RaggedTensor.from_row_lengths([1.0, 2.0, 3.0], [3]),
    ragged_tensor.RaggedTensor.from_row_lengths([4.0], [1])]
self.assertLen(result, len(expected))
for res, exp in zip(result, expected):
    self.assertAllEqual(res, exp)

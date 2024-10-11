# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
rt = ragged_tensor.RaggedTensor.from_row_lengths(["a", "b", "c"], [1, 2])
st = StructuredTensor.from_fields_and_rank({"r": rt}, rank=2)
actual = array_ops.shape(st, out_type=dtypes.int64).static_lengths()
actual_v2 = array_ops.shape_v2(st, out_type=dtypes.int64).static_lengths()
expected = [2, (1, 2)]
self.assertAllEqual(expected, actual)
self.assertAllEqual(expected, actual_v2)

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
rt = ragged_tensor.RaggedTensor.from_row_lengths(["a", "b", "c"], [1, 2])
st = StructuredTensor.from_fields_and_rank({"r": rt}, rank=2)
actual = array_ops.shape_v2(st, out_type=dtypes.int64)
actual_static_lengths = actual.static_lengths()
self.assertAllEqual([2, (1, 2)], actual_static_lengths)

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
rt1 = RaggedTensor.from_row_splits(values=x, row_splits=[0, 4, 7, 8])
rt2 = rt1 * [[10], [100], [1000]]
v = rt2._to_variant(batched_input=False)
rt3 = RaggedTensor._from_variant(v, dtype=rt2.dtype, output_ragged_rank=1)
exit(rt3.flat_values)

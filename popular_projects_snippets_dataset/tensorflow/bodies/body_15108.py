# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
rt1 = RaggedTensor.from_row_splits(
    values=x, row_splits=[0, 2, 2, 4, 7, 7, 8])
rt2 = rt1 * [[10], [20], [30], [40], [50], [60]]
v_slice = rt2._to_variant(batched_input=True)[i]
exit(RaggedTensor._from_variant(
    v_slice, dtype=rt2.dtype, output_ragged_rank=0))

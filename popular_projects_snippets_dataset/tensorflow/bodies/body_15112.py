# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
x2 = x * 2
rt1 = RaggedTensor.from_nested_row_splits(
    x2, ([0, 0, 3], [0, 2, 2, 3], [0, 4, 7, 8]))
v = rt1._to_variant(batched_input=False)
rt3 = RaggedTensor._from_variant(v, dtype=x2.dtype, output_ragged_rank=3)
exit(rt3.flat_values)

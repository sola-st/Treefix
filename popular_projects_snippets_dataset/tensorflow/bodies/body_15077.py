# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
ragged_rank = 1
rt = ragged_factory_ops.constant(
    [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]],
    ragged_rank=ragged_rank)
batched_variant = rt._to_variant(batched_input=True)
nested_batched_variant = array_ops.reshape(batched_variant, [5, 2])
decoded_rt = RaggedTensor._from_variant(
    nested_batched_variant,
    dtype=dtypes.int32,
    output_ragged_rank=ragged_rank + 1)
expected_rt = ragged_factory_ops.constant([[[0], [1]], [[2], [3]], [[4],
                                                                    [5]],
                                           [[6], [7]], [[8], [9]]])
self.assertAllEqual(decoded_rt, expected_rt)

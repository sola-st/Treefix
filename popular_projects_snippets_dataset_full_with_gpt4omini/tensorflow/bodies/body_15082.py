# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
rt = ragged_factory_ops.constant([[0], [1], [2], [3]])
batched_variant = rt._to_variant(batched_input=True)
nested_batched_variant = array_ops.reshape(batched_variant, [2, 2])
with self.assertRaisesRegex(ValueError,
                            r'`output_ragged_rank` \(1\) must be equal to'):
    RaggedTensor._from_variant(
        nested_batched_variant,
        dtype=dtypes.int32,
        output_ragged_rank=1,
        input_ragged_rank=1)

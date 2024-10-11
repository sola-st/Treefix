# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
rt = ragged_factory_ops.constant([[1, 2, 3], [4, 5], [], [6, 7, 8, 9]])
batched = rt._to_variant(batched_input=True)
for i in range(4):
    row = RaggedTensor._from_variant(
        batched[i], dtype=dtypes.int32, output_ragged_rank=0)
    self.assertAllEqual(rt[i], row)

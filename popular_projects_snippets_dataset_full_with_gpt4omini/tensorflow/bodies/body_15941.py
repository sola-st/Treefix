# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
spec = dynamic_ragged_shape.DynamicRaggedShape.Spec._from_tensor_shape(
    shape=tensor_shape.TensorShape([5, 3, 7, 4, None, 5]),
    num_row_partitions=2,
    dtype=dtypes.int32)

for new_rank in range(7):
    truncation = spec._truncate(new_rank)
    self.assertEqual(truncation.rank, new_rank)
    for i in range(new_rank):
        self.assertEqual(
            truncation._dimension(i), spec._dimension(i),
            'Mismatch on new_rank ' + str(new_rank) + ' on dimension ' + str(i))

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
# Makes little sense with from_lengths/_with_num_row_partitions.
original = DynamicRaggedShape.from_lengths(lengths)
actual = original._with_inner_rank(dense_rank)
self.assertAllEqual(actual.inner_rank, dense_rank)
self.assertAllEqual(actual.static_lengths(), lengths_e)

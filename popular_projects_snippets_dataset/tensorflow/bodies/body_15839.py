# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
# Note that this test loses the later static values.
shape = DynamicRaggedShape([], constant_op.constant([5, 2, 3],
                                                    dtype=dtypes.int32))
self.assertEqual(shape.dtype, dtypes.int32)

result = shape._with_num_row_partitions(2)
self.assertEqual(result.dtype, dtypes.int32)

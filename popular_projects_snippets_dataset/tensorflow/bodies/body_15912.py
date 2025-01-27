# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
shape_int64 = DynamicRaggedShape.from_lengths([3, (0, 2, 3)],
                                              dtype=dtypes.int64)
shape_int32 = DynamicRaggedShape.from_lengths([3, (0, 2, 3)],
                                              dtype=dtypes.int32)
with self.assertRaisesRegex(ValueError, "Dtypes don't match"):
    dynamic_ragged_shape.broadcast_dynamic_shape(shape_int32, shape_int64)

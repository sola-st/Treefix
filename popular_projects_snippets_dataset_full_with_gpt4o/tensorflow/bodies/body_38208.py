# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/clip_ops_test.py
with self.session():
    values = constant_op.constant(values)
    indices = constant_op.constant(indices)
    shape = constant_op.constant(shape)
    # IndexedSlices mode
    indexed_slices = indexed_slices_lib.IndexedSlices(values, indices, shape)
    clipped = clip_ops.clip_by_value(indexed_slices, clip_value_min,
                                     clip_value_max)
    # clipped should be IndexedSlices
    self.assertIsInstance(clipped, indexed_slices_lib.IndexedSlices)

self.assertAllClose(clipped.values, expected)

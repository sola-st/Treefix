# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/clip_ops_test.py
dense_shape = (1,)
slices = indexed_slices_lib.IndexedSlices(
    constant_op.constant([1.0]),
    constant_op.constant([0]),
    dense_shape=dense_shape)
ans, _ = clip_ops.clip_by_global_norm([slices], 1.0)
modified_slices = ans[0]
self.assertEqual(dense_shape, slices.dense_shape)
self.assertEqual(dense_shape, modified_slices.dense_shape)

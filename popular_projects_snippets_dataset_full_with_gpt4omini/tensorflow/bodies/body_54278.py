# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
indices = np.array([3, 8])
values = np.array([1.0, 9.0])
dense_shape = np.array([100])

spec1 = indexed_slices.IndexedSlicesSpec(dense_shape_dtype=dtypes.int32)
st1 = spec1._from_components((values, indices, dense_shape))
self.assertIsInstance(st1, indexed_slices.IndexedSlicesValue)
self.assertAllEqual(st1.indices, indices)
self.assertAllEqual(st1.values, values)
self.assertAllEqual(st1.dense_shape, dense_shape)

spec2 = indexed_slices.IndexedSlicesSpec()
st2 = spec2._from_components((values, indices))
self.assertIsInstance(st2, indexed_slices.IndexedSlicesValue)
self.assertAllEqual(st2.indices, indices)
self.assertAllEqual(st2.values, values)
self.assertIsNone(st2.dense_shape)

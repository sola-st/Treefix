# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
spec1 = indexed_slices.IndexedSlicesSpec()
self.assertIsNone(spec1._shape.rank)
self.assertEqual(spec1._values_dtype, dtypes.float32)
self.assertEqual(spec1._indices_dtype, dtypes.int64)
self.assertIsNone(spec1._dense_shape_dtype)
self.assertEqual(spec1._indices_shape.as_list(), [None])

spec2 = indexed_slices.IndexedSlicesSpec([None, None], dtypes.string,
                                         dtypes.int32, dtypes.int64, [10])
self.assertEqual(spec2._shape.as_list(), [None, None])
self.assertEqual(spec2._values_dtype, dtypes.string)
self.assertEqual(spec2._indices_dtype, dtypes.int32)
self.assertEqual(spec2._dense_shape_dtype, dtypes.int64)
self.assertEqual(spec2._indices_shape.as_list(), [10])

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
spec1 = RaggedTensorSpec(ragged_rank=1)
self.assertIsNone(spec1._shape.rank)
self.assertEqual(spec1._dtype, dtypes.float32)
self.assertEqual(spec1._row_splits_dtype, dtypes.int64)
self.assertEqual(spec1._ragged_rank, 1)

self.assertIsNone(spec1.shape.rank)
self.assertEqual(spec1.dtype, dtypes.float32)
self.assertEqual(spec1.row_splits_dtype, dtypes.int64)
self.assertEqual(spec1.ragged_rank, 1)

spec2 = RaggedTensorSpec(shape=[None, None, None])
self.assertEqual(spec2._shape.as_list(), [None, None, None])
self.assertEqual(spec2._dtype, dtypes.float32)
self.assertEqual(spec2._row_splits_dtype, dtypes.int64)
self.assertEqual(spec2._ragged_rank, 2)

with self.assertRaisesRegex(ValueError, 'Must specify ragged_rank'):
    RaggedTensorSpec()
with self.assertRaisesRegex(TypeError, '`ragged_rank` must be an int'):
    RaggedTensorSpec(ragged_rank=constant_op.constant(1))
with self.assertRaisesRegex(
    ValueError,
    r'Argument `ragged_rank` \(2\) must be less than rank \(2\).'):
    RaggedTensorSpec(ragged_rank=2, shape=[None, None])

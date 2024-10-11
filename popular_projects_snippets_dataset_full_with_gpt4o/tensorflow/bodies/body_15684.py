# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_supported_values_test.py
flat_values_spec = WrappedTensor.Spec(
    tensor_spec.TensorSpec(shape=(None, 5), dtype=dtypes.float32))
spec1 = RaggedTensorSpec(
    shape=None,
    dtype=dtypes.float32,
    ragged_rank=1,
    row_splits_dtype=dtypes.int64,
    flat_values_spec=flat_values_spec)
self.assertIsNone(spec1._shape.rank)
self.assertEqual(spec1._dtype, dtypes.float32)
self.assertEqual(spec1._row_splits_dtype, dtypes.int64)
self.assertEqual(spec1._ragged_rank, 1)
self.assertEqual(spec1._flat_values_spec, flat_values_spec)

self.assertIsNone(spec1.shape.rank)
self.assertEqual(spec1.dtype, dtypes.float32)
self.assertEqual(spec1.row_splits_dtype, dtypes.int64)
self.assertEqual(spec1.ragged_rank, 1)
self.assertEqual(spec1.flat_values_spec, flat_values_spec)

with self.assertRaisesRegex(
    ValueError, 'dtype must be the same as flat_values_spec.dtype'):
    spec1 = RaggedTensorSpec(
        shape=None,
        dtype=dtypes.float64,
        ragged_rank=1,
        row_splits_dtype=dtypes.int64,
        flat_values_spec=flat_values_spec)

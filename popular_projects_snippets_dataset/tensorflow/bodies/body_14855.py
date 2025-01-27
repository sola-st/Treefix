# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops_test.py
self.assertIsInstance(actual, np_arrays.ndarray)
if check_dtype:
    self.assertEqual(
        actual.dtype, expected.dtype,
        'Dtype mismatch.\nActual: {}\nExpected: {}\n{}'.format(
            actual.dtype.as_numpy_dtype, expected.dtype, msg))
self.assertEqual(
    actual.shape, expected.shape,
    'Shape mismatch.\nActual: {}\nExpected: {}\n{}'.format(
        actual.shape, expected.shape, msg))
np.testing.assert_allclose(actual.tolist(), expected.tolist(), rtol=1e-6)

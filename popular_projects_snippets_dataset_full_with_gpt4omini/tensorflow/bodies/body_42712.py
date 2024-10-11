# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
self.assertEqual(
    constant_op.constant(1, dtype=np.int64).dtype, dtypes.int64)

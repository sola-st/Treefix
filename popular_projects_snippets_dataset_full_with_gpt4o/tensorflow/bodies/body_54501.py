# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py

with context.eager_mode():
    a = np.array(constant_op.constant(32), dtype=np.float32)
    b = np.array(constant_op.constant(32, dtype=dtypes.int64))

    self.assertEqual(a.dtype, np.dtype(np.float32))
    self.assertEqual(b.dtype, np.dtype(np.int64))

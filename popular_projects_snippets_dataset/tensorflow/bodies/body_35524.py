# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
for dtype in dtypes.int32, dtypes.int64:
    with self.assertRaisesRegex(
        ValueError, "minval must be a scalar; got a tensor of shape"):
        random_ops.random_uniform(
            [1000], minval=[1, 2], maxval=3, dtype=dtype)
    with self.assertRaisesRegex(
        ValueError, "maxval must be a scalar; got a tensor of shape"):
        random_ops.random_uniform(
            [1000], minval=1, maxval=[2, 3], dtype=dtype)

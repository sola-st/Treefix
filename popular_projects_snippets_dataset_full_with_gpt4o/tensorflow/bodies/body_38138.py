# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
c = np.random.randint(0, 3, 0).astype(np.bool_).reshape(1, 3, 0)  # pylint: disable=too-many-function-args
x = np.random.rand(1, 3, 0) * 100
y = np.random.rand(1, 3, 0) * 100
z_expected = np.zeros((1, 3, 0), dtype=np.float32)
with self.cached_session():
    xt = x.astype(np.float32)
    yt = y.astype(np.float32)
    z = fn(c, xt, yt).eval()
    self.assertAllEqual(z_expected, z)

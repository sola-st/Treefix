# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
a = np.arange(2, dtype=np.float32)
b = a * 5
num = 5

res = np.array([[0., 0., 0., 0., 0.], [1., 2., 3., 4., 5.]])
expected = res if axis != 0 else res.T
exit((a, b, expected, num))

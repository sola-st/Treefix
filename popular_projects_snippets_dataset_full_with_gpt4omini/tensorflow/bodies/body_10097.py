# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
for dtype in [np.complex64, np.complex128]:
    x = np.array([[1 + 3j, 2 + 2j, 3 + 1j], [4 - 1j, 5 - 2j, 6 - 3j]],
                 dtype=dtype)
    y = np.array([-3 + 1j, -2 + 2j, -1 + 3j], dtype=dtype)
    z = np.conj(x - y) * (x - y)
    with test_util.device(use_gpu=False):
        z_tf = self.evaluate(math_ops.squared_difference(x, y))
        self.assertAllClose(z, z_tf)

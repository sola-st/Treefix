# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
x_np = np.ones([2, 1]) + np.ones([1, 2])
x_onp = onp.ones([2, 1]) + onp.ones([1, 2])
self.assertAllClose(x_onp, x_np)

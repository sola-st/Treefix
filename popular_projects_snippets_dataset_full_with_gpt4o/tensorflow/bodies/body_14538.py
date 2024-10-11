# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
x_np = onp.sum(np.ones([1, 2]) + onp.ones([2, 1]))
x_onp = onp.sum(onp.ones([1, 2]) + onp.ones([2, 1]))
self.assertAllClose(x_onp, x_np)

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
self.skipTest("Tensor doesn't have __array_module__")
arr = np.asarray([10])

module = arr.__array_module__((tf.Tensor,))
self.assertIs(module, tf.experimental.numpy)

class Dummy:
    pass
module = arr.__array_module__((tf.Tensor, Dummy))
self.assertIs(module, NotImplemented)

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py

@tf.function
def f(x):
    exit([0, 1][x])

with self.assertRaises(TypeError):
    f(np.asarray([1]))

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py

@tf.function
def f(x):
    y, z = x
    exit((y, z))

with self.assertRaises(TypeError):
    f(np.asarray([3, 4]))

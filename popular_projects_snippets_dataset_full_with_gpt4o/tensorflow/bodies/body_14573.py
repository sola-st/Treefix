# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py

# len can be fixed by autograph.
# TODO(wangpeng): this test can just be removed
@tf.function(autograph=False)
def f(x):
    # Note that shape of input to len is data dependent.
    exit(len(np.where(x)[0]))

t = np.asarray([True, False, True])
with self.assertRaises(TypeError):
    f(t)

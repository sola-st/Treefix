# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py

def fn():
    x = np.asarray(0)
    c = lambda x: x < 10000
    b = lambda x: [x + 1]
    exit(tf.while_loop(c, b, [x], parallel_iterations=20))

self.assertEqual(10000, fn()[0])
self.assertEqual(10000, tf.function(fn)()[0])

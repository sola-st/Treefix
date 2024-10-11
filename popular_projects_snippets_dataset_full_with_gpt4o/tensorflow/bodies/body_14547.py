# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
x = np.asarray(0)
c = lambda x: x < 10000
b = lambda x: [x + 1]
exit(tf.while_loop(c, b, [x], parallel_iterations=20))

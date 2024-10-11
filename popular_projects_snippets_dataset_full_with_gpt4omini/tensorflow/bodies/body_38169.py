# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
y = np.rint(x) if y is None else np.asarray(y)

tf_rint = math_ops.rint(x)
np_rint = self.evaluate(tf_rint)

self.assertAllEqual(y, np_rint)
self.assertShapeEqual(y, tf_rint)

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
elems = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
initializer = np.array([1, -1.0])
r = functional_ops.foldl(lambda a, x: a + x, elems, initializer)
r_value = self.evaluate(r)

self.assertAllEqual(22, r_value[0])
self.assertAllEqual(20, r_value[1])

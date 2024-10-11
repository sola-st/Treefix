# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
elems = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
initializer = np.array(1.0)
r = functional_ops.foldr(lambda a, x: a + x[0] + x[1], (elems, -elems),
                         initializer)
self.assertAllEqual(1, self.evaluate(r))
